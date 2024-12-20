from django.urls import path
from .import views

urlpatterns = [
    path("", views.homePage, name = "home"),
    path('create_employee/', views.createEmployeee, name = "create-employee"),
    path('employee_list/', views.employeeList, name = 'employee-list'),
    path('employee-edit/<int:pid>', views.edit_employee, name="edit_employee"),
    path('delete_employee/<int:pid>', views.delete_employee, name="delete_employee"),
    path('leave-status/<int:pid>', views.leave_status, name="leave_status"),
]
