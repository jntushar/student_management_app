from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add_student'),
    path('student/<int:stu_id>', views.student_info, name='student_info'),
    path('search/', views.search, name='search'),
    path('contactus/', views.contactus, name='contactus'),
]
