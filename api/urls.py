from django.urls import path,include
from . import views
urlpatterns = [
    path('students/',views.studentsViews),
    path('students/<int:pk>/',views.studentDetailViews),
    path('employees/',views.employee.as_view()),
    path('employees/<int:pk>/',views.employeeDetail.as_view()),
]
