from django.db import models
from django.utils.translation import gettext

from users.models import UserList

class Category(models.Model):
    tag = models.TextField(max_length=50, blank=True, null=True)
    # common_matchesX are for tagging reference and generally shouldnt be seen by the user
    common_matches1 = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.tag
    
    class Meta:
        ordering = ('tag',)
        verbose_name_plural = gettext('Categories')


class Transaction(models.Model):
    charge_date = models.DateField(null=True)
    charge_name = models.CharField(max_length=255)
    amount = models.FloatField(default=0)
    tag = models.ForeignKey(Category, verbose_name="tag", on_delete=models.CASCADE)
    notes = models.CharField(max_length=255, blank=True)
    name = models.ForeignKey(UserList, verbose_name="user", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        entryID = str(self.charge_date) + " - " + str(self.charge_name) + " - " + str(self.amount)
        return entryID
    
    class Meta:
        ordering = ('charge_date',)