from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def homePage(request):
    return render(request, "index.html")


def createEmployeee(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        department = request.POST['department']
        post = request.POST['post']
        emp_obj = Employee.objects.create(name=name,dob=dob,doj=doj,address=address,city=city,state=state,zipcode=zipcode,country=country,department=department,post=post)
        messages.success(request, "Employee created successfully")
        return redirect('employee-list')
    return render(request, 'create_employee.html')

def employeeList(request):
    emp_data = Employee.objects.filter()
    d = {'employee':emp_data}
    return render(request, 'employee_list.html',d)


def edit_employee(request, pid):
    emp_data =Employee.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        department = request.POST['department']
        post = request.POST['post']
        emp_obj = Employee.objects.filter(id=pid).update(name=name,dob=dob,doj=doj,address=address,city=city,state=state,zipcode=zipcode,country=country,department=department,post=post)
        messages.success(request, "Employee Updated successfully")
        return redirect('employee-list')
    return render(request, 'edit_employee.html', {'emp_data':emp_data})


def delete_employee(request, pid):
    data = Employee.objects.get(id=pid)
    data.delete()
    messages.success(request, "Employee Deleted successfully")
    return redirect('employee-list')


def leave_status(request, pid):
    data = Employee.objects.get(id=pid)
    if data.on_leave:
        data.on_leave = False
    else:
        data.leave_count = data.leave_count + 1
        data.on_leave = True
    data.save()
    messages.success(request, "Employee leave status Changed successfully.")
    return redirect('employee-list')
