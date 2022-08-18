from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


## creating router objects
router = DefaultRouter()

## register StudentViewSet with router
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'), name='rest_framework'),
    path('gettoken/', obtain_auth_token),
]
