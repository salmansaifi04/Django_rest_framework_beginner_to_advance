from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

## creating router objects
router = DefaultRouter()

## register StudentViewSet with router
router.register('studentapi', views.StudentReadOnlyViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
