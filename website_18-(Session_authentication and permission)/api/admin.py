from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']


## SuperUser
## superuser
## salman@123

## adminuser
## adminuser
## salman@123

## normaluser
## user1
## salman@123