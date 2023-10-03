from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Course, Class, Enrollment, Lecturer, Student, Semester


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['semester', 'year']
        widgets = {
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['semester', 'code', 'name']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
        }

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['number', 'course', 'enrollments', 'lecturer']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'enrollments': forms.Select(attrs={'class': 'form-control'}),
            'lecturer': forms.Select(attrs={'class': 'form-control'}),
        }

    enrollments = forms.ModelMultipleChoiceField(
        queryset=Enrollment.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

class ClassUpdateForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['number', 'enrollments', 'lecturer']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'enrollments': forms.Select(attrs={'class': 'form-control'}),
            'lecturer': forms.Select(attrs={'class': 'form-control'}),
        }

    enrollments = forms.ModelMultipleChoiceField(
        queryset=Enrollment.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

class ClassLecturerForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['lecturer']
        widgets = {
            'lecturer': forms.Select(attrs={'class': 'form-control'}),
        }

class ClassEnrolmentForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['enrollments']
        widgets = {
            'enrollments': forms.Select(attrs={'class': 'form-control'}),
        }

    enrollments = forms.ModelMultipleChoiceField(
        queryset=Enrollment.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

class UserRegistrationForm1(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']

class UserRegistrationForm2(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']

class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['dob', 'lecturerInfo']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'lecturerInfo': forms.Select(attrs={'class': 'form-control'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['dob', 'studentInfo']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'studentInfo': forms.Select(attrs={'class': 'form-control'}),
        }

