from django.urls import path

from attendance.views import HomePageView, list_semesters, detail_semester, detail_course, list_courses, list_classes, \
    detail_class, list_lecturers, detail_lecturer, list_students, detail_student, create_semester_form, create_semester, \
    CourseCreateView, ClassCreateView, register_user_lecturer, register_user_student, LecturerCreateView, \
    StudentCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("semesters", list_semesters, name="semesters"),
    path("semesters/<int:id>", detail_semester,
         name="detail_semester"),
    path("semesters/create_form", create_semester_form,
         name="create_semester_form"),
    path("semesters/create", create_semester,
         name="create_semester"),
    path("courses", list_courses, name="courses"),
    path("courses/<int:id>", detail_course,
         name="detail_course"),
    path("courses/create", CourseCreateView.as_view(),
         name="create_course"),
    path("classes", list_classes, name="classes"),
    path("classes/<int:id>", detail_class,
         name="detail_class"),
    path("classes/create", ClassCreateView.as_view(),
         name="create_class"),
    path("lecturers", list_lecturers, name="lecturers"),
    path("lecturers/<int:id>", detail_lecturer,
         name="detail_lecturer"),
    path("lecturers/register/create", LecturerCreateView.as_view(),
         name="create_lecturer"),
    path("students", list_students, name="students"),
    path("students/<int:id>", detail_student,
         name="detail_student"),
    path("students/register/create", StudentCreateView.as_view(),
         name="create_student"),
    path('lecturers/register', register_user_lecturer, name='register_user_lecturer'),
    path('students/register', register_user_student, name='register_user_student'),
]