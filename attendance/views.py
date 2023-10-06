from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from attendance.forms import CourseForm, ClassForm, UserRegistrationForm1, UserRegistrationForm2, LecturerForm, \
    StudentForm, ClassLecturerForm, ClassEnrolmentForm, SemesterForm, CourseUpdateForm, ClassUpdateForm, \
    UploadExcelForm, AttendanceForm
from attendance.models import Semester, Course, Class, Lecturer, Student, Enrollment, Attendance, CollegeDay
import pandas as pd


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
            if user.is_staff and user.is_superuser:
                login(request, user)
                return redirect('home')
            else:
                error_message = "You don't have administrator access."
        else:
            error_message = "Invalid username or password."

    return render(request, 'administrator_login.html', {'error_message': error_message})

# login for lecturers
def lecturer_login(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            lecturer = Lecturer.objects.get(lecturerInfo__username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None and lecturer:
                login(request, user)
                return redirect('classlist_lecturer')
            else:
                error_message = "Invalid username or password."
        except ObjectDoesNotExist:
            error_message = "Invalid username or you don't have lecturer access."

    return render(request, 'lecturer_login.html', {'error_message': error_message})

# login for students
def student_login(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            student = Student.objects.get(studentInfo__username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None and student:
                login(request, user)
                return redirect('classlist_student')
            else:
                error_message = "Invalid username or password."
        except ObjectDoesNotExist:
            error_message = "Invalid username or you don't have student access."

    return render(request, 'student_login.html', {'error_message': error_message})

# logout for everyone
def logoutUser(request):
    logout(request)

    return redirect('home')

# upload Excel file and register them as students
def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            for _, row in df.iterrows():
                dob = row['DOB']
                first_name = row['First Name']
                last_name = row['Last Name']
                username = row['User Name']
                user = User.objects.create(username=username, first_name=first_name, last_name=last_name)
                student = Student.objects.create(dob=dob, studentInfo=user)
            return redirect('home')
    else:
        form = UploadExcelForm()
    return render(request, 'upload_excel.html', {'form': form})

# showing classes that a specific lecturer assigned
def classlist_lecturer(request):
    lecturer_username = request.user.username
    classes_by_lecturer = Class.objects.filter(lecturer__lecturerInfo__username=lecturer_username)

    return render(request, 'classlist_lecturer.html', {'classes_by_lecturer': classes_by_lecturer})

# showing classes that a specific student attends
def classlist_student(request):
    student_username = request.user.username
    classes_by_student = Class.objects.filter(enrollments__student__studentInfo__username=student_username)

    return render(request, 'classlist_student.html', {'classes_by_student': classes_by_student})

# marking attendance for lecturer
def mark_attendance(request, class_id):
    # Retrieve the class based on the provided class_id
    class_obj = get_object_or_404(Class, id=class_id)

    if request.method == 'POST':
        # Handle form submission
        form = AttendanceForm(request.POST, class_obj=class_obj)  # Pass class_obj to the form
        if form.is_valid():
            date = form.cleaned_data['date']
            attendance_data = form.cleaned_data['attendance_data']

            # Loop through students and mark attendance
            for student in class_obj.enrollments.all():
                status = attendance_data.get(str(student.id), 'absent')
                CollegeDay.objects.create(date=date, classInfo=class_obj, students=student, status=status)

            return redirect('classlist_lecturer')

    else:
        # Display the form to mark attendance
        form = AttendanceForm(class_obj=class_obj)  # Pass class_obj to the form

    context = {
        'form': form,
        'class': class_obj,
    }

    return render(request, 'mark_attendance.html', context)



# checking attendance for students
def view_attendance(request, class_id):
    selected_class = get_object_or_404(Class, pk=class_id)
    student_username = request.user.username

    # Check if the student is enrolled in the class
    enrollment = selected_class.enrollments.filter(student__studentInfo__username=student_username).first()

    if enrollment:
        attendances = Attendance.objects.filter(class_info=selected_class, enrollment=enrollment)
        return render(request, 'view_attendance.html', {'class': selected_class, 'attendances': attendances})
    else:
        return HttpResponseForbidden("You are not enrolled in this class.")

