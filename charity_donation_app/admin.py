from django.contrib import admin
from .models import Category, Institution, Donation, User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Donation)
admin.site.register(User, UserAdmin)
