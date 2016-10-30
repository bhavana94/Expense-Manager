from django.contrib import admin

# Register your models here.

from .models import Account, Category, Transactions

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transactions)
