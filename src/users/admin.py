from django.contrib import admin
from django.contrib.auth.models import Group

from users import models

admin.site.unregister(Group)


@admin.register(models.User)
class User(admin.ModelAdmin):
    search_fields = ('username', 'first_name', 'last_name')
