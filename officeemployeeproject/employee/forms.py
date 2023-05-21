from django import forms
from .models import Employee, Department, Role

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
