from django.urls import path

from attendance.views import HomePageView, list_semesters, detail_semester, detail_course, list_courses, list_classes, \
    detail_class, list_lecturers, detail_lecturer, list_students, detail_student, create_semester_form, create_semester, \
    CourseCreateView, ClassCreateView, register_user_lecturer, register_user_student, LecturerCreateView, \
    StudentCreateView, ClassLecturerUpdateView, ClassStudentEnrolView, ClassLecturerAssignView, \
    remove_class_lecturer, remove_class_enrollment, SemesterUpdateView, SemesterDeleteView, CourseUpdateView, \
    CourseDeleteView, ClassUpdateView, ClassDeleteView, LecturerUpdateView, LecturerDeleteView, StudentUpdateView, \
    StudentDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("semesters", list_semesters, name="semesters"),
    path("semesters/<int:id>", detail_semester,
         name="detail_semester"),
    path("semesters/create_form", create_semester_form,
         name="create_semester_form"),
    path("semesters/create", create_semester,
         name="create_semester"),
    path("semesters/update/<int:id>", SemesterUpdateView.as_view(),
         name="update_semester"),
    path("semester/delete/<int:id>", SemesterDeleteView.as_view()
         , name="delete_semester"),
    path("courses", list_courses, name="courses"),
    path("courses/<int:id>", detail_course,
         name="detail_course"),
    path("courses/create", CourseCreateView.as_view(),
         name="create_course"),
    path("courses/update/<int:id>", CourseUpdateView.as_view()
         , name="update_course_view"),
    path("courses/delete/<int:id>", CourseDeleteView.as_view()
         , name="delete_course_view"),
    path("classes", list_classes, name="classes"),
    path("classes/<int:id>", detail_class,
         name="detail_class"),
    path("classes/create", ClassCreateView.as_view(),
         name="create_class"),
    path("classes/update/<int:id>", ClassUpdateView.as_view()
         , name="update_class_view"),
    path("classes/delete/<int:id>", ClassDeleteView.as_view()
         , name="delete_class_view"),
    path("classes/assignLecturer/<int:pk>", ClassLecturerAssignView.as_view()
         , name="assign_class_lecturer_view"),
    path("classes/removeLecturer/<int:id>",  remove_class_lecturer
         , name="remove_class_lecturer"),
    path("classes/updateLecturer/<int:pk>", ClassLecturerUpdateView.as_view()
         , name="update_class_lecturer_view"),
    path("classes/enrol/<int:pk>", ClassStudentEnrolView.as_view()
         , name="enrol_class_enrolment_view"),
    path("classes/removeEnrol/<int:id>/<int:enrollment_id>", remove_class_enrollment
         , name="remove_class_enrollment"),
    path("lecturers", list_lecturers, name="lecturers"),
    path("lecturers/<int:id>", detail_lecturer,
         name="detail_lecturer"),
    path("lecturers/register/create", LecturerCreateView.as_view(),
         name="create_lecturer"),
    path("lecturers/update/<int:id>", LecturerUpdateView.as_view()
         , name="update_lecturer_view"),
    path("lecturers/delete/<int:id>", LecturerDeleteView.as_view()
         , name="delete_lecturer_view"),
    path("students", list_students, name="students"),
    path("students/<int:id>", detail_student,
         name="detail_student"),
    path("students/register/create", StudentCreateView.as_view(),
         name="create_student"),
    path("students/update/<int:id>", StudentUpdateView.as_view()
         , name="update_student_view"),
    path("students/delete/<int:id>", StudentDeleteView.as_view()
         , name="delete_student_view"),
    path('lecturers/register', register_user_lecturer, name='register_user_lecturer'),
    path('students/register', register_user_student, name='register_user_student'),
]