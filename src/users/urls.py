from django.urls import include, path
from rest_framework.routers import SimpleRouter

from users import views

app_name = 'users'

urlpatterns = [
    # Djoser + SimpleJWT
    path('', include('djoser.urls.jwt')),
]

router = SimpleRouter()

router.register('users', views.User, 'users')

urlpatterns += router.urls
