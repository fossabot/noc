# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## fm.reportreboots
##----------------------------------------------------------------------
## Copyright (C) 2007-2016 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import datetime
## Django modules
from django import forms
from django.db import connection
from django.contrib.admin.widgets import AdminDateWidget
## NOC modules
from noc.lib.app.simplereport import SimpleReport, TableColumn, PredefinedReport
from noc.fm.models.reboot import Reboot
from noc.sa.models.managedobject import ManagedObject
from noc.sa.models.useraccess import UserAccess
from noc.core.translation import ugettext as _


class ReportForm(forms.Form):
    interval = forms.ChoiceField(choices=[
        (0, _("Range")),
        (1, _("1 day")),
        (7, _("1 week")),
        (30, _("1 month"))
    ], label=_("Inteval"))
    from_date = forms.CharField(
        widget=AdminDateWidget,
        label=_("From Date"),
        required=False
    )
    to_date = forms.CharField(
        widget=AdminDateWidget,
        label=_("To Date"),
        required=False
    )


class ReportRebootsApplication(SimpleReport):
    title = _("Reboots")
    form = ReportForm
    predefined_reports = {
        "1d": PredefinedReport(
            _("Reboots (1 day)"), {
                "interval": 1
            }
        ),
        "7d": PredefinedReport(
            _("Reboots (7 days)"), {
                "interval": 7
            }
        ),
        "30d": PredefinedReport(
            _("Reboot (30 day)"), {
                "interval": 30
            }
        )
    }

    def get_data(self, request, interval, from_date=None, to_date=None, **kwargs):
        interval = int(interval)
        if not from_date:
            interval = 1
        if interval:
            ts = datetime.datetime.now() - datetime.timedelta(days=interval)
            match = {
                "ts": {
                    "$gte": ts
                }
            }
        else:
            t0 = datetime.datetime.strptime(from_date, "%d.%m.%Y")
            if not to_date:
                t1 = datetime.datetime.now()
            else:
                t1 = datetime.datetime.strptime(to_date, "%d.%m.%Y") + datetime.timedelta(days=1)
            match = {
                "ts": {
                    "$gte": t0,
                    "$lte": t1
                }
            }
        pipeline = [
            {
                "$match": match
            },
            {"$group": {"_id": "$object", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]
        data = Reboot._get_collection().aggregate(pipeline)
        data = data["result"]
        # Get managed objects
        if not request.user.is_superuser:
            id_perm = [mo.id for mo in ManagedObject.objects.filter(
                administrative_domain__in=UserAccess.get_domains(request.user))]
            ids = [x["_id"] for x in data if x["_id"] in id_perm]
        else:
            ids = [x["_id"] for x in data]
        mo_names = {}  # mo id -> mo name
        cursor = connection.cursor()
        while ids:
            chunk = [str(x) for x in ids[:500]]
            ids = ids[500:]
            cursor.execute("""
                SELECT id, address, name
                FROM sa_managedobject
                WHERE id IN (%s)""" % ", ".join(chunk))
            mo_names.update(dict([(c[0], c[1:3]) for c in cursor]))
        #
        if not request.user.is_superuser:
            data = [
                (mo_names.get(x["_id"], "---")[1],
                 mo_names.get(x["_id"], "---")[0], x["count"])
                for x in data if x["_id"] in id_perm
            ]
        else:
            data = [
                (mo_names.get(x["_id"], "---")[1],
                 mo_names.get(x["_id"], "---")[0], x["count"])
                for x in data
            ]

        return self.from_dataset(
            title=self.title,
            columns=[
                _("Managed Object"), _("Address"),
                TableColumn(_("Reboots"), align="right",
                            format="numeric", total="sum")
            ],
            data=data,
            enumerate=True
        )
