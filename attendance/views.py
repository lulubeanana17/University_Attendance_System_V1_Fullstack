from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from attendance.forms import CourseForm, ClassForm, UserRegistrationForm1, UserRegistrationForm2, LecturerForm, \
    StudentForm, ClassLecturerForm, ClassEnrolmentForm, SemesterForm, CourseUpdateForm, ClassUpdateForm
from attendance.models import Semester, Course, Class, Lecturer, Student, Enrollment


class HomePageView(ListView):
    template_name = "home.html"
    model = Semester

# show semesters
def list_semesters(request):
    data = Semester.objects.all()
    content = {'semesters': data}
    return render(request, "list_semesters.html", content)

# show list of semesters
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

# create semesters
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

# create semesters
def create_semester_form(request):
    return render(request,
                  'create_semester_form.html', {})

# update semesters
class SemesterUpdateView(UpdateView):
    template_name = "update_semester_view.html"
    model = Semester
    form_class = SemesterForm
    pk_url_kwarg = 'id'

# delete semesters
class SemesterDeleteView(DeleteView):
    template_name = "delete_semester_view.html"
    model = Semester
    success_url = reverse_lazy("semesters")
    pk_url_kwarg = 'id'

# show courses
def list_courses(request):
    data = Course.objects.all()
    content = {'courses': data}
    return render(request, "list_courses.html", content)

# show list of courses
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

# create courses
class CourseCreateView(CreateView):
    template_name = "create_course_view.html"
    model = Course
    form_class = CourseForm

# update courses
class CourseUpdateView(UpdateView):
    template_name = "update_course_view.html"
    model = Course
    form_class = CourseUpdateForm
    pk_url_kwarg = 'id'

# delete courses
class CourseDeleteView(DeleteView):
    template_name = "delete_course_view.html"
    model = Course
    success_url = reverse_lazy("courses")
    pk_url_kwarg = 'id'

# show classes
def list_classes(request):
    data = Class.objects.all()
    content = {'classes': data}
    return render(request, "list_classes.html", content)

# show list of classes
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

# create classes
class ClassCreateView(CreateView):
    template_name = "create_class_view.html"
    model = Class
    form_class = ClassForm

# update classes
class ClassUpdateView(UpdateView):
    template_name = "update_class_view.html"
    model = Class
    form_class = ClassUpdateForm
    pk_url_kwarg = 'id'

# delete classes
class ClassDeleteView(DeleteView):
    template_name = "delete_class_view.html"
    model = Class
    success_url = reverse_lazy("classes")
    pk_url_kwarg = 'id'

# show lecturers
def list_lecturers(request):
    data = Lecturer.objects.all()
    content = {'lecturers': data}
    return render(request, "list_lecturers.html", content)

#show list of lecturers
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

# create lecturers
class LecturerCreateView(CreateView):
    template_name = "create_lecturer_view.html"
    model = Lecturer
    form_class = LecturerForm

# update lecturers
class LecturerUpdateView(UpdateView):
    template_name = "update_lecturer_view.html"
    model = Lecturer
    form_class = LecturerForm
    pk_url_kwarg = 'id'

# delete lecturers
class LecturerDeleteView(DeleteView):
    template_name = "delete_lecturer_view.html"
    model = Lecturer
    success_url = reverse_lazy("lecturers")
    pk_url_kwarg = 'id'

# show students
def list_students(request):
    data = Student.objects.all()
    content = {'students': data}
    return render(request, "list_students.html", content)

#show list of students
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

#create students
class StudentCreateView(CreateView):
    template_name = "create_student_view.html"
    model = Student
    form_class = StudentForm

# update students
class StudentUpdateView(UpdateView):
    template_name = "update_student_view.html"
    model = Student
    form_class = StudentForm
    pk_url_kwarg = 'id'

# delete students
class StudentDeleteView(DeleteView):
    template_name = "delete_student_view.html"
    model = Student
    success_url = reverse_lazy("students")
    pk_url_kwarg = 'id'

# create lecturers
def register_user_lecturer(request):
    if request.method == 'POST':
        form = UserRegistrationForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_lecturer')
    else:
        form = UserRegistrationForm1()

    return render(request, 'user_lecturer_register.html', {'form': form})

# create students
def register_user_student(request):
    if request.method == 'POST':
        form = UserRegistrationForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_student')
    else:
        form = UserRegistrationForm2()

    return render(request, 'user_student_register.html', {'form': form})

# assign lecturer to classes
class ClassLecturerAssignView(UpdateView):
    template_name = "assign_class_lecturer_view.html"
    model = Class
    form_class = ClassLecturerForm

# remove lecturer to classes
def remove_class_lecturer(request, id):
    data = get_object_or_404(Class, pk=id)
    data.lecturer = None
    data.save()

    return redirect('classes')

# change lecturer to classes
class ClassLecturerUpdateView(UpdateView):
    template_name = "update_class_lecturer_view.html"
    model = Class
    form_class = ClassLecturerForm

# enroll student to classes
class ClassStudentEnrolView(UpdateView):
    template_name = "enrol_class_enrolment_view.html"
    model = Class
    form_class = ClassEnrolmentForm

# remove students to classes
def remove_class_enrollment(request, id, enrollment_id):
    data = get_object_or_404(Class, pk=id)
    try:
        enrol_data = get_object_or_404(Enrollment, pk=enrollment_id)

        data.enrollments.remove(enrol_data)
    except Enrollment.DoesNotExist:
        pass

    return redirect('classes')

# login for administrator
def administrator_login(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect('home')
            else:
                error_message = "You don't have administrator access."
        else:
            error_message = "Invalid username or password."

    return render(request, 'administrator_login.html', {'error_message': error_message})

# logout for everyone
def logoutUser(request):
    logout(request)

    return redirect('home')

