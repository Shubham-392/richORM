from richorm.db.models import base
from richorm.db.models.fields import models

class TestClass(base.Model):
    name = models.CharField(max_length=7)
    phone_number = models.IntegerField()

