from .models import Employees
from django import forms

class employees_form(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"



 