# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (C) 2007-2012 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Django modules
from django.db import models
# Third-party modules
from south.db import db


class Migration:
    def forwards(self):
        Activator = db.mock_model(model_name='Activator',
            db_table='sa_activator', db_tablespace='',
            pk_field_name='id', pk_field_type=models.AutoField)
        db.add_column("sa_managedobjectselector", "filter_activator",
            models.ForeignKey(Activator,
                verbose_name="Filter by Activator", null=True,
                blank=True))

    def backwards(self):
        db.delete_column("sa_managedobjectselector",
            "filter_activator_id")
