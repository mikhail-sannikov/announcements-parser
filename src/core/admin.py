from django.contrib import admin

from core import models

admin.site.register(models.Company)


@admin.register(models.CompanyMember)
class CompanyMember(admin.ModelAdmin):
    list_display = ('company', 'member')
    search_fields = ('company', 'member')


@admin.register(models.Announcement)
class Announcement(admin.ModelAdmin):
    list_display = ('title', 'author', 'views_amount')
    search_fields = ('title', 'author')
