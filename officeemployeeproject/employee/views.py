from django.shortcuts import render, redirect
from .models import *
from .forms import EmployeeForm
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def list_view(request):
    emp_list = Employee.objects.all()
    return render(request, 'list.html', {'emp_list':emp_list})

def add_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('add_emp')

    return render(request, 'add.html', {'form':form})

def remove_view(request, id=0):
    if id:
        try:
            data = Employee.objects.get(id=id)
            data.delete()
            return redirect('remove_emp')
        except:
            return HttpResponse('Please Enter a valid Employee Id')
    emp_list = Employee.objects.all()
    return render(request, 'remove.html', {'emp_list':emp_list})
def filter_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('d-name')
        role = request.POST.get('role')

        emp_list = Employee.objects.all()
        if name:
            emp_list = emp_list.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            emp_list = emp_list.filter(dept__name__icontains=dept)
        if role:
            emp_list = emp_list.filter(role__name__icontains=role)
        context = {
                'emp_list':emp_list
        }
        return render(request, 'list.html', context)
    elif request.method == 'GET':
        return render(request, 'filter.html')
    else:
        return HttpResponse('An Exception occured')
