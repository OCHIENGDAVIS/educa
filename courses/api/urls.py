from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('subjects/', views.SubjectListAPIView.as_view(), name='subject_list'),
    path('subject/<pk>', views.SubjectDetailAPIView.as_view(), name='subject_detail'),
]
