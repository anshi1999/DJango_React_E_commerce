from django.contrib import admin
from userauths.models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display =['full_name', 'gender', 'country']
    list_editable =['gender', 'country']
    search_fields =['full_name', 'date']
    list_filter = ['date']

admin.site.register(User)
admin.site.register(Profile)
