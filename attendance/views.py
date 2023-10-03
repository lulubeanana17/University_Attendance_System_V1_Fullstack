from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from attendance.forms import CourseForm, ClassForm, UserRegistrationForm1, UserRegistrationForm2, LecturerForm, \
    StudentForm
from attendance.models import Semester, Course, Class, Lecturer, Student


class HomePageView(ListView):
    template_name = "home.html"
    model = Semester

def list_semesters(request):
    data = Semester.objects.all()
    content = {'semesters': data}
    return render(request, "list_semesters.html", content)

def detail_semester(request, id):
    error_message = ""
    try:
        data = Semester.objects.get(id=id)
    except Semester.DoesNotExist:
        error_message = "The semester does not exist"
        data = None
    return render(request, "detail_semester.html",
                  {"semester": data,
                   "error_message": error_message})

def create_semester(request):
    semester = request.POST.get("semester_semester")
    year = request.POST.get("semester_year")
    message = "new semester " + semester + " - " + year + " has been created"
    try:
        Semester.objects.create(semester=semester, year=year)
    except:
        message = "some error there"
    return render(request, 'create_semester.html',
                  {'message': message})


def create_semester_form(request):
    return render(request,
                  'create_semester_form.html', {})

def list_courses(request):
    data = Course.objects.all()
    content = {'courses': data}
    return render(request, "list_courses.html", content)

def detail_course(request, id):
    error_message = ""
    try:
        data = Course.objects.get(id=id)
    except Course.DoesNotExist:
        error_message = "The category does not exist"
        data = None
    return render(request, "detail_course.html",
                  {"course": data,
                   "error_message": error_message})

class CourseCreateView(CreateView):
    template_name = "create_course_view.html"
    model = Course
    form_class = CourseForm

def list_classes(request):
    data = Class.objects.all()
    content = {'classes': data}
    return render(request, "list_classes.html", content)

def detail_class(request, id):
    error_message = ""
    try:
        data = Class.objects.get(id=id)
    except Class.DoesNotExist:
        error_message = "The category does not exist"
        data = None
    return render(request, "detail_class.html",
                  {"class": data,
                   "error_message": error_message})

class ClassCreateView(CreateView):
    template_name = "create_class_view.html"
    model = Class
    form_class = ClassForm

def list_lecturers(request):
    data = Lecturer.objects.all()
    content = {'lecturers': data}
    return render(request, "list_lecturers.html", content)

def detail_lecturer(request, id):
    error_message = ""
    try:
        data = Lecturer.objects.get(id=id)
    except Lecturer.DoesNotExist:
        error_message = "The category does not exist"
        data = None
    return render(request, "detail_lecturer.html",
                  {"lecturer": data,
                   "error_message": error_message})

class LecturerCreateView(CreateView):
    template_name = "create_lecturer_view.html"
    model = Lecturer
    form_class = LecturerForm

def list_students(request):
    data = Student.objects.all()
    content = {'students': data}
    return render(request, "list_students.html", content)

def detail_student(request, id):
    error_message = ""
    try:
        data = Student.objects.get(id=id)
    except Student.DoesNotExist:
        error_message = "The category does not exist"
        data = None
    return render(request, "detail_student.html",
                  {"student": data,
                   "error_message": error_message})

class StudentCreateView(CreateView):
    template_name = "create_student_view.html"
    model = Student
    form_class = StudentForm

def register_user_lecturer(request):
    if request.method == 'POST':
        form = UserRegistrationForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_lecturer')
    else:
        form = UserRegistrationForm1()

    return render(request, 'user_lecturer_register.html', {'form': form})

def register_user_student(request):
    if request.method == 'POST':
        form = UserRegistrationForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_student')
    else:
        form = UserRegistrationForm2()

    return render(request, 'user_student_register.html', {'form': form})