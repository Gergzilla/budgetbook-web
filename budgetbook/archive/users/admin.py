from django.contrib import admin

from .models import CustomUser, UserList
# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, BudgetAdmin)
admin.site.register(UserList, BudgetAdmin)