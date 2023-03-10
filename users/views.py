from django.shortcuts import redirect, render
from .forms import EmployeeRegistrationForm
from django.shortcuts import render
from .models import Employee



def register_employee(request):
    form=EmployeeRegistrationForm()
    return render(request,"register_employee.html",{
        "form":form,
        "name":"Daisi Caroline",
    })
def register_employee(request):
    if request.method=="POST":
        form=EmployeeRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EmployeeRegistrationForm()
    return render(request,"register_employee.html",{"form":form})

def employee_list(request):
    employees=Employee.objects.all()
    return render(request,"employee_list.html",{ "employees":employees})

def employee_profile(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,"employee_profile.html",{"employee":employee})

def edit_employee(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeRegistrationForm(request.POST,instance=employee)
        if form.is_valid():
             form.save()
             return redirect("employee_profile",id=employee.id)

    else: 
        form=EmployeeRegistrationForm(instance=employee) 
        return render(request,"edit_employee.html",{"form":form})  

    