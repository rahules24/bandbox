from django.db import models


class SlipModel(models.Model):
    slip_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.slip_id
