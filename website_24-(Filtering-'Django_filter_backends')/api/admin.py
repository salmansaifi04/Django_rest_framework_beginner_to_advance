from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'passby']


## superuser
## salman@123

## user1
## salman@123

## user2
## salman@123
