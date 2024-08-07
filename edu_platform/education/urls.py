# education/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('courses/manage/', views.manage_courses, name='manage_courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('assessment/<int:assessment_id>/', views.assessment_detail, name='assessment_detail'),
    path('forum/<int:forum_id>/', views.forum_detail, name='forum_detail'),
    path('forum/<int:forum_id>/create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/create_comment/', views.create_comment, name='create_comment'),
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/mark_read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Custom login view
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),  # Custom logout view
]
