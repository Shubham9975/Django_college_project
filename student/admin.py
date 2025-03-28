from django.contrib import admin
from .models import Student, Parent
from django.utils.html import format_html
from django import forms

# Register your models here.

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'father_mobile', 'mother_name', 'mother_mobile')
    search_fields = ('father_name', 'father_mobile', 'mother_name', 'mother_mobile')
    list_filter = ('father_name', 'mother_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'gender', 'date_of_birth', 'student_class', 'joining_date', 'mobile_number', 'admission_number', 'section', 'student_image')
    search_fields = ('first_name', 'last_name', 'student_id', 'student_class','admission_number')
    list_filter = ('gender', 'student_class', 'section')

    def student_image(self, obj):
        if obj.student_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.student_image.url)
        return "-"
    student_image.allow_tags = True
    student_image.short_description = "Student Image"