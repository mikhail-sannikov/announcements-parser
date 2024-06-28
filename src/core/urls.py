from django.urls import path
from rest_framework.routers import SimpleRouter

from core import views

app_name = 'core'

urlpatterns = [path('companies/<int:pk>/', views.Company.as_view(), name='companies')]

router = SimpleRouter()

router.register('announcements', views.Announcement, 'announcements')

urlpatterns += router.urls
