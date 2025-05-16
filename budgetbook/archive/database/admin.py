from django.contrib import admin

from .models import Category, Transaction

# Register your models here.

class BudgetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, BudgetAdmin)
admin.site.register(Transaction, BudgetAdmin)
