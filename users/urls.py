from .views import edit_employee, register_employee, employee_profile
from django.urls import path
from .views import register_employee,employee_list
from .views import employee_profile
from django.urls import reverse



urlpatterns = [
    path("",register_employee,name="register_employee"),
    path("list/",employee_list,name="employee_list"),
    path("profile/<int:id>/",employee_profile,name="employee_profile"),
    path("edit/<int:id>/",edit_employee,name="edit_employee"),

    
]