from django.urls import path

from .views import StudentRegistration, StudentEnrollCourseView

urlpatterns = [
    path('register/', StudentRegistration.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
]
