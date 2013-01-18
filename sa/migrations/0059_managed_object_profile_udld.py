from south.db import db
from django.db import models

class Migration:
    d_types = ["udld"]

    def forwards(self):
        for d in self.d_types:
            db.add_column("sa_managedobjectprofile",
                "enable_%s_discovery" % d,
                models.BooleanField("", default=True))
            db.add_column("sa_managedobjectprofile",
                "%s_discovery_min_interval" % d,
                models.IntegerField("", default=600))
            db.add_column("sa_managedobjectprofile",
                "%s_discovery_max_interval" % d,
                models.IntegerField("", default=86400))

    def backwards(self):
        for d in self.d_types:
            db.delete_column("sa_managedobjectprofile",
                "enable_%s_discovery" % d)
            db.delete_column("sa_managedobjectprofile",
                "%s_discovery_min_interval" % d)
            db.delete_column("sa_managedobjectprofile",
                "%s_discovery_max_interval" % d)
