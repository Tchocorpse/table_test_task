from django.db import models


class TaskTable(models.Model):
    id = models.AutoField(primary_key=True)

    date = models.DateTimeField(verbose_name="Date", auto_now_add=True, blank=False, null=False)
    name = models.CharField(verbose_name="Name", max_length=255, blank=False, null=False)
    quantity = models.IntegerField(verbose_name="Quantity", blank=False, null=False)
    distance = models.IntegerField(verbose_name="Distance", blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated = models.DateTimeField(auto_now=True, blank=False, null=False)
