from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from pages.models import CustomUser
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'birthdate', 'country', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ['email']
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(CustomUser)