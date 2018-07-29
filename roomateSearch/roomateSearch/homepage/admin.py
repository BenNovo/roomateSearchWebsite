from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from homepage.models import RoomateUser
# Register your models here.

class RoomateUserInline(admin.StackedInline):
    model = RoomateUser
    verbose_name = 'RoomateUser'
    
class UserAdmin(BaseUserAdmin):
    inlines = (RoomateUserInline,)
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)