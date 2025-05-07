from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def list_employees(request):
    employees = Employee.objects.all()
    return render(request, "employee/list.html",{"employees":employees})

def create_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employee-list")
    return render(request,"employee/create.html",{"form":form})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("employee-list")
    return render(request, "employee/update.html",{"form":form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee,pk=pk)
    employee.delete()
    return redirect("employee-list")