from django.contrib import admin
from .models import UserModel

class UserModelAdmin(admin.ModelAdmin):
    list_display=('username', 'theme')

admin.site.register(UserModel, UserModelAdmin)
