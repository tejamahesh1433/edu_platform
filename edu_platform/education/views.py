from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Course, Enrollment, Assessment, Grade, Notification, Forum, Post, Comment, Week, Grade
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
from .forms import FeedbackForm

# Custom Login and Logout Views
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_teacher:
                return reverse_lazy('teacher_dashboard')
            else:
                return reverse_lazy('student_dashboard')
        return super().get_success_url()

    def form_valid(self, form):
        print("CustomLoginView is being used")
        return super().form_valid(form)

# Student Dashboard View
@login_required
def student_dashboard(request):
    user = request.user
    if not user.is_student:
        return redirect('teacher_dashboard')

    courses = Enrollment.objects.filter(student=user).select_related('course')
    notifications = Notification.objects.filter(user=user, read=False)

    context = {
        'courses': courses,
        'notifications': notifications
    }
    return render(request, 'education/student_dashboard.html', context)

# Teacher Dashboard View
@login_required
def teacher_dashboard(request):
    user = request.user
    if not user.is_teacher:
        return redirect('student_dashboard')

    courses = Course.objects.filter(teacher=user)
    notifications = Notification.objects.filter(user=user, read=False)

    context = {
        'courses': courses,
        'notifications': notifications
    }
    return render(request, 'education/teacher_dashboard.html', context)

# Manage Courses View
@login_required
def manage_courses(request):
    user = request.user
    if not user.is_teacher:
        return redirect('student_dashboard')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Course.objects.create(title=title, description=description, teacher=user)
        return redirect('manage_courses')

    courses = Course.objects.filter(teacher=user)
    context = {
        'courses': courses
    }
    return render(request, 'education/manage_courses.html', context)

# Course Detail View
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user != course.teacher and not Enrollment.objects.filter(course=course, student=request.user).exists():
        messages.error(request, "You do not have access to this course.")
        return redirect('student_dashboard')

    assessments = Assessment.objects.filter(course=course)
    forums = Forum.objects.filter(course=course)
    context = {
        'course': course,
        'assessments': assessments,
        'forums': forums
    }
    return render(request, 'education/course_detail.html', context)

# Assessment Detail View
@login_required
def assessment_detail(request, assessment_id):
    assessment = get_object_or_404(Assessment, id=assessment_id)
    if request.user != assessment.course.teacher and not Enrollment.objects.filter(course=assessment.course, student=request.user).exists():
        messages.error(request, "You do not have access to this assessment.")
        return redirect('student_dashboard')

    grades = Grade.objects.filter(assessment=assessment)
    context = {
        'assessment': assessment,
        'grades': grades
    }
    return render(request, 'education/assessment_detail.html', context)

# Forum Detail View
@login_required
def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.user != forum.course.teacher and not Enrollment.objects.filter(course=forum.course, student=request.user).exists():
        messages.error(request, "You do not have access to this forum.")
        return redirect('student_dashboard')

    posts = Post.objects.filter(forum=forum)
    context = {
        'forum': forum,
        'posts': posts
    }
    return render(request, 'education/forum_detail.html', context)

# Create Post View
@login_required
def create_post(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Post.objects.create(forum=forum, author=request.user, content=content)
        return redirect('forum_detail', forum_id=forum.id)
    return render(request, 'education/create_post.html', {'forum': forum})

# Create Comment View
@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)
        return redirect('forum_detail', forum_id=post.forum.id)
    return render(request, 'education/create_comment.html', {'post': post})

# Notifications View
@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'education/notifications.html', {'notifications': notifications})

# Mark Notification as Read View
@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.read = True
    notification.save()
    return redirect('notifications')

# Dashboard Insights View
@login_required
def dashboard_insights(request):
    return render(request, 'education/dashboard_insights.html')

# Dashboard Reports View
@login_required
def dashboard_reports(request):
    return render(request, 'education/dashboard_reports.html')

# Adaptive Learning View
@login_required
def adaptive_learning(request):
    return render(request, 'education/adaptive_learning.html')

# Dashboard Overview View
@login_required
def dashboard_overview(request):
    return render(request, 'education/dashboard_overview.html')

# Dashboard Scheduling View
@login_required
def dashboard_scheduling(request):
    return render(request, 'education/dashboard_scheduling.html')

# Analytics View
@login_required
def analytics_view(request):
    context = {
        'data': "This is your analytics data."
    }
    return render(request, 'education/analytics.html', context)

# API View to Get Course Data
def get_course_data(request):
    courses = Course.objects.all()
    data = {
        'labels': [course.title for course in courses],
        'completion_rates': [course.completion_rate for course in courses],  # Assuming you store completion rates in your Course model
    }
    return JsonResponse(data)

# API View to Get User Analytics
def user_analytics(request):
    data = {
        'labels': ['January', 'February', 'March'],
        'values': [100, 200, 150]
    }
    return JsonResponse(data)

# API View to Get Course Analytics
def course_analytics(request):
    data = {
        'labels': ['Course 1', 'Course 2', 'Course 3'],
        'values': [80, 90, 70]
    }
    return JsonResponse(data)

# API View to Get Engagement Analytics
def engagement_analytics(request):
    data = {
        'labels': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        'values': [50, 60, 70, 80]
    }
    return JsonResponse(data)

# API View to Get Financial Analytics
def financial_analytics(request):
    data = {
        'labels': ['Revenue', 'Expenses', 'Profit'],
        'values': [30000, 20000, 10000]
    }
    return JsonResponse(data)

# Assessment Tools View
@login_required
def assessment_tools(request):
    return render(request, 'tools/assessment.html')

# Add Course View
@login_required
def add_course(request):
    user = request.user
    if not user.is_teacher:
        return redirect('student_dashboard')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Course.objects.create(title=title, description=description, teacher=user)
        return redirect('manage_courses')
    
    return render(request, 'education/add_course.html')

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.user != course.teacher:
        messages.error(request, "You do not have permission to edit this course.")
        return redirect('manage_courses')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if not title or not description:
            messages.error(request, "Both title and description are required.")
            return render(request, 'education/edit_course.html', {'course': course})
        
        course.title = title
        course.description = description
        course.save()
        messages.success(request, "Course updated successfully.")
        return redirect('course_detail', course_id=course.id)

    return render(request, 'education/edit_course.html', {'course': course})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user != course.teacher:
        messages.error(request, "You do not have permission to delete this course.")
        return redirect('manage_courses')

    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course deleted successfully.")
        return redirect('manage_courses')

    context = {
        'course': course
    }
    return render(request, 'education/delete_course.html', context)

# View and Edit Course Syllabus
@login_required
def course_syllabus(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if not (request.user == course.teacher or Enrollment.objects.filter(course=course, student=request.user).exists()):
        if request.user.is_teacher:
            return redirect('teacher_dashboard')
        else:
            return redirect('student_dashboard')
    
    weeks = Week.objects.filter(course=course).order_by('week_number')

    context = {
        'course': course,
        'weeks': weeks,
    }
    return render(request, 'education/course_syllabus.html', context)

@login_required
def manage_enrollment(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user != course.teacher:
        messages.error(request, "You do not have permission to manage enrollments for this course.")
        return redirect('manage_courses')

    students = Enrollment.objects.filter(course=course).select_related('student')

    context = {
        'course': course,
        'students': students,
    }
    return render(request, 'education/manage_enrollment.html', context)

@login_required
def grading_view(request, course_id=None):
    course = None
    grades = None

    if course_id:
        course = get_object_or_404(Course, id=course_id)

        # Check if the current user is the teacher of the course
        if request.user != course.teacher:
            messages.error(request, "You do not have permission to manage grades for this course.")
            return redirect('teacher_dashboard')

        # Retrieve grades only if the user is the teacher of the course
        grades = Grade.objects.filter(assessment__course=course).select_related('student', 'assessment')

    context = {
        'course': course,
        'grades': grades,
    }

    return render(request, 'education/grading.html', context)

@login_required
def grading_courses(request):
    user = request.user
    if not user.is_teacher:
        return redirect('student_dashboard')

    courses = Course.objects.filter(teacher=user)
    
    context = {
        'courses': courses,
    }
    return render(request, 'education/grading_courses.html', context)

@login_required
def grading_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user != course.teacher:
        messages.error(request, "You do not have permission to grade this course.")
        return redirect('grading_courses')

    students = Enrollment.objects.filter(course=course)
    
    context = {
        'course': course,
        'students': students,
    }
    return render(request, 'education/grading_students.html', context)

@login_required
def grade_student(request, course_id, student_id):
    course = get_object_or_404(Course, id=course_id)
    student = get_object_or_404(User, id=student_id)
    
    if request.user != course.teacher:
        messages.error(request, "You do not have permission to grade this course.")
        return redirect('grading_courses')
    
    if request.method == 'POST':
        grade_value = request.POST.get('grade')
        assessment_id = request.POST.get('assessment_id')
        assessment = get_object_or_404(Assessment, id=assessment_id, course=course)
        Grade.objects.create(student=student, assessment=assessment, grade=grade_value)
        messages.success(request, "Grade successfully recorded.")
        return redirect('grading_students', course_id=course.id)

    assessments = Assessment.objects.filter(course=course)
    grades = Grade.objects.filter(student=student, assessment__course=course)
    
    context = {
        'course': course,
        'student': student,
        'assessments': assessments,
        'grades': grades,
    }
    return render(request, 'education/grade_student.html', context)

@login_required
def grading_course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.enrollments.all()

    context = {
        'course': course,
        'students': students,
    }
    return render(request, 'education/grading_course_detail.html', context)

@login_required
def grading_course_detail(request, course_id):
    context = {
        # context variables here
    }
    return render(request, 'education/grading_course_detail.html', context)

@login_required
def specific_course_grading(request, course_id):
    # Logic to handle the request
    context = {'course_id': course_id}
    return render(request, 'education/specific_course_grading.html', context)

@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the feedback here (e.g., save it to a database or send an email)
            # For now, let's just add a message and redirect
            messages.success(request, "Thank you for your feedback!")
            return redirect('some_other_view')
    else:
        form = FeedbackForm()
    
    return render(request, 'education/submit_feedback.html', {'form': form})
