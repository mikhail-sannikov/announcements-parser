from django.db.models import F
from rest_framework.generics import RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core import filters, models, serializers


class Company(RetrieveAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanyRead


class Announcement(ModelViewSet):
    queryset = models.Announcement.objects.all()
    filterset_class = filters.Announcement

    def get_serializer_class(self) -> serializers:
        if self.action in ('retrieve', 'list'):
            return serializers.AnnouncementRead
        return serializers.AnnouncementWrite

    def retrieve(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        models.Announcement.objects.filter(pk=kwargs['pk']).update(views_amount=F('views_amount') + 1)
        return super().retrieve(request, *args, **kwargs)
