from django.db import models


# Create your models here.
class Data(models.Model):
    message = models.TextField(default="")

    class Meta:
        db_table = "data"

    def __str__(self):
        return self.message
