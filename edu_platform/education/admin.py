# D:\project32\edu_platform\education\admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course, Enrollment, Assessment, Grade, Notification, Forum, Post, Comment

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_student', 'is_teacher')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_student', 'is_teacher')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Assessment)
admin.site.register(Grade)
admin.site.register(Notification)
admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Comment)
