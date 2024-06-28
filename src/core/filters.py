from django.db.models import Q, QuerySet
from django_filters import rest_framework as filters

from core import models


class Announcement(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(field_name='author__username', lookup_expr='icontains')
    company_name = filters.CharFilter(field_name='company__name', lookup_expr='icontains')
    views_amount = filters.RangeFilter()

    combine = filters.CharFilter(method='filter_combine')

    class Meta:
        model = models.Announcement
        fields = ()

    @staticmethod
    def filter_combine(queryset: QuerySet[models.Announcement], name: str, value: str) -> QuerySet[models.Announcement]:
        return queryset.filter(Q(title__icontains=value) | Q(author__username__icontains=value))
