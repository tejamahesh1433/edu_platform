from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Course, Enrollment, Assessment, Grade, Notification, Forum, Post, Comment
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

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

@login_required
def student_dashboard(request):
    user = request.user
    if not user.is_student:
        return redirect('teacher_dashboard')

    # Add any additional context if necessary
    courses = Enrollment.objects.filter(student=user).select_related('course')
    notifications = Notification.objects.filter(user=user, read=False)

    context = {
        'courses': courses,
        'notifications': notifications
    }
    return render(request, 'education/student_dashboard.html', context)

@login_required
def teacher_dashboard(request):
    user = request.user
    if not user.is_teacher:
        return redirect('student_dashboard')

    # Add any additional context if necessary
    courses = Course.objects.filter(teacher=user)
    notifications = Notification.objects.filter(user=user, read=False)

    context = {
        'courses': courses,
        'notifications': notifications
    }
    return render(request, 'education/teacher_dashboard.html', context)

@login_required
def manage_courses(request):
    user = request.user
    if not user.is_teacher:
        return redirect('student_dashboard')

    courses = Course.objects.filter(teacher=user)
    context = {
        'courses': courses
    }
    return render(request, 'education/manage_courses.html', context)

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

@login_required
def create_post(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Post.objects.create(forum=forum, author=request.user, content=content)
        return redirect('forum_detail', forum_id=forum.id)
    return render(request, 'education/create_post.html', {'forum': forum})

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)
        return redirect('forum_detail', forum_id=post.forum.id)
    return render(request, 'education/create_comment.html', {'post': post})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'education/notifications.html', {'notifications': notifications})

@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.read = True
    notification.save()
    return redirect('notifications')
