from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Lecturer(models.Model):
    dob = models.DateField()
    lecturerInfo = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.lecturerInfo.first_name + self.lecturerInfo.last_name

    def get_absolute_url(self):
        return reverse("lecturers")

class Student(models.Model):
    dob = models.DateField()
    studentInfo = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.studentInfo.first_name + self.studentInfo.last_name

    def get_absolute_url(self):
        return reverse("students")

class Semester(models.Model):
    semester = models.CharField(max_length=255)
    year = models.CharField(max_length=255)

    def __str__(self):
        return self.semester + " " + self.year

class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " - " + self.semester.semester + " " + self.semester.year

    def get_absolute_url(self):
        return reverse("courses")

class Enrollment(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.studentInfo.first_name + " " + self.student.studentInfo.last_name

class Class(models.Model):
    number = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='Class')
    enrollments = models.ManyToManyField(Enrollment, blank=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name='Class')

    def __str__(self):
        return self.course.name + " " + self.number + " - " + self.course.semester.semester + " " + self.course.semester.year

    def get_absolute_url(self):
        return reverse("classes")

class CollegeDay(models.Model):
    date = models.DateField()
    classInfo = models.ForeignKey(Class, null=True, blank=True, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.date
