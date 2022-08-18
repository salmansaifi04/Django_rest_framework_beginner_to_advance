from django.contrib import admin
from django.urls import path
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/<int:pk>/', views.student_data),
    path('stu/', views.student_list),
]
