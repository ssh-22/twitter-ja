from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Account, Relationship

# Define an inline admin descriptor for Account model
# which acts a bit like a singleton
class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'account'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (AccountInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Relationshipモデルを登録する
@admin.register(Relationship)
class AdminRelationship(admin.ModelAdmin):
    pass
