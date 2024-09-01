from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Student)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','roll','name','city']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','price']



