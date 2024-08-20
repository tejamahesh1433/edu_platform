from django.urls import include, path
from . import views

urlpatterns = [
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
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('dashboard/insights/', views.dashboard_insights, name='dashboard_insights'),
    path('dashboard/reports/', views.dashboard_reports, name='dashboard_reports'), 
    path('adaptive_learning/', views.adaptive_learning, name='adaptive_learning'),  # Ensure this line is included
    path('tools/assessment/', views.assessment_tools, name='assessment-tools'),
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
    path('grading/', views.general_grading, name='grading'),

]
