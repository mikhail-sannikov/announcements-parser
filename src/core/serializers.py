from rest_framework import serializers
from users.serializers import User

from core import models


class CompanyRead(serializers.ModelSerializer):
    members = User(read_only=True, many=True)

    class Meta:
        model = models.Company
        fields = '__all__'


class AnnouncementRead(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = models.Announcement
        exclude = ('company', 'author')


class AnnouncementWrite(serializers.ModelSerializer):
    class Meta:
        model = models.Announcement
        exclude = ('views_amount',)
