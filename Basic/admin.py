from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from django.contrib.auth.models import User

from .models import Staff

# Register your models here.
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2",'email','first_name','last_name'),
            },
        ),
    )
    pass
admin.site.unregister(User)
admin.site.register(User,UserAdmin)

@admin.register(Staff)
class CustomeAdmin(admin.ModelAdmin):
    list_display = ['user','Age','Sex','Position','Salary','Native_Addr','Phone']
    list_per_page = 10
    autocomplete_fields = ['user']