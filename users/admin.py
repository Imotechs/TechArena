from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_diplay = ('surname', 'last_name','student_id')

admin.site.register(Student,StudentAdmin)
