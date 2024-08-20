"""
URL configuration for edu_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from education.views import assessment_tools  # Make sure to import the view
from education.views import get_course_data
from django.contrib import admin
from django.urls import path, include
from education import views  # Ensure 'views' is imported
from django.contrib.auth.views import (
    PasswordChangeView, 
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('courses/manage/', views.manage_courses, name='manage_courses'),
    path('course/add/', views.add_course, name='add_course'),  # Ensure this line is included
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('course/<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('assessment/<int:assessment_id>/', views.assessment_detail, name='assessment_detail'),
    path('forum/<int:forum_id>/', views.forum_detail, name='forum_detail'),
    path('forum/<int:forum_id>/create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/create_comment/', views.create_comment, name='create_comment'),
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/mark_read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('dashboard/insights/', views.dashboard_insights, name='dashboard_insights'),
    path('dashboard/reports/', views.dashboard_reports, name='dashboard_reports'),
    path('adaptive_learning/', views.adaptive_learning, name='adaptive_learning'),
    path('dashboard/scheduling/', views.dashboard_scheduling, name='dashboard_scheduling'),  # Ensure this view exists
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),  # Ensure this is correctly imported
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('tools/analytics/', views.analytics_view, name='analytics_view'),
    path('api/course-data/', get_course_data, name='course-data'),
    path('api/user-analytics/', views.user_analytics, name='user-analytics'),
    path('api/course-analytics/', views.course_analytics, name='course-analytics'),
    path('api/engagement-analytics/', views.engagement_analytics, name='engagement-analytics'),
    path('api/financial-analytics/', views.financial_analytics, name='financial-analytics'),
    path('tools/assessment/', views.assessment_tools, name='assessment-tools'),  # Ensure this path is included
    path('', include('django.contrib.auth.urls')),  # Include the authentication URLs (login, logout)
    path('courses/syllabus/', views.course_syllabus, name='course_syllabus'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('course/<int:course_id>/syllabus/', views.course_syllabus, name='course_syllabus'),
    path('course/<int:course_id>/manage_enrollment/', views.manage_enrollment, name='manage_enrollment'),
    path('course/<int:course_id>/grading/', views.grading_view, name='grading'),
    path('grading/', views.grading_courses, name='grading_courses'),
    path('grading/<int:course_id>/', views.grading_students, name='grading_students'),
    path('grading/<int:course_id>/<int:student_id>/', views.grade_student, name='grade_student'),
    path('grading/course/<int:course_id>/', views.grading_course_detail, name='grading_course_detail'),
    path('manage_courses/', views.manage_courses, name='manage_courses'),
    path('course/<int:course_id>/grading/', views.specific_course_grading, name='grading'),
    path('grading/', views.grading_view, name='grading'),
    path('grading/<int:course_id>/', views.grading_view, name='grading'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),

]
