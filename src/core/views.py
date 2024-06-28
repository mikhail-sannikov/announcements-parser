from rest_framework.generics import RetrieveAPIView
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
