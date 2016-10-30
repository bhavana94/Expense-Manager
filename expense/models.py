from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


# Create your models here.

TRANSACTION_TYPE = [
    ('credit', 'Credit'),
    ('debit', 'Debit')

]


class TimeStamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_('Created On'))
    modified_on = models.DateTimeField(auto_now=True, verbose_name=_('Modified On'))

    class Meta:
        abstract = True


class Account(TimeStamp):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_no = models.IntegerField(primary_key=True, blank=False)
    monthly_budget = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.account_no


class Category(TimeStamp):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=63, unique=True, blank=True, null=True, verbose_name='Slug (Auto Fill)')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)


class Transactions(TimeStamp):

    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE)
    comment = models.CharField(max_length=100, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.amount
