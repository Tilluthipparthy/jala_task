from django.shortcuts import render,redirect
from .form import employees_form
from .models import Employees
from .models import Image

# Create your views here.

def home(request):
    return render(request,'homepage.html')
def base(request):
    return render(request,'base.html')

def employee_form_page(request):
    if request.method == 'GET':
        emp_form = employees_form()
        return render(request, 'create_employeepage.html', {'emp_form': emp_form})

    else:
        emp_form = employees_form(request.POST)
        if emp_form.is_valid():
            emp_form.save()
            return redirect('/base')
        else:
            # Return the same page WITH errors
            return render(request, 'create_employeepage.html', {'emp_form': emp_form})
        

def employee_search_page(request):
    query1=request.GET.get('search_emp_name_value')
    query2=request.GET.get('search_emp_number_value')
    if query1 and query2:
        all_employees=Employees.objects.filter(emp_fname=query1,emp_number=query2)
        return render(request, 'search_employeepage.html', {'all_employees': all_employees})
    else:
        all_employees = Employees.objects.all()
        return render(request, 'search_employeepage.html', {'all_employees': all_employees})

    # update button 




def update_employee(request, id):
    employee_object = Employees.objects.get(pk=id)

    if request.method == 'GET':
        emp_form = employees_form(instance=employee_object)
        return render(request, 'create_employeepage.html', {'emp_form': emp_form})

    elif 'delete_btn' in request.POST:
        employee_object.delete()
        return redirect('/employee_search_page')

    else:
        emp_form = employees_form(request.POST, instance=employee_object)
        if emp_form.is_valid():

            emp_form.save()   # ✅ FIX 1 (you missed parentheses)
            return redirect('/employee_search_page')

        else:
            return render(request, 'create_employeepage.html', {'emp_form': emp_form})
    
def multipletabs(request):
    return render(request,'multiple_tabs.html')
def menu(request):
    return render(request,'menu.html')
def autocomplete(request):
        return render(request,'autocomplete.html')
def collapse(request):
    return render(request,'collapse.html')

def image(request):
    if request.method=="POST":
        get_imagename=request.POST.get('img_name')
        get_imagefile=request.FILES.get('img_file')
        if get_imagename and get_imagefile:
            x=Image.objects.create(img_name=get_imagename,image=get_imagefile)
            x.save()
            return redirect('/image')
    x=Image.objects.all()
    return render(request,'image.html',{'img':x})

def slider(request):
    return render(request,'slider.html')
def tooltip(request):
    return render(request,'tooltip.html')
def popup(request):
    return render(request,'popup.html')
def links(request):
    return render(request,'links.html')
def css(request):
    return render(request,'css.html')
def iframe(request):
    return render(request,'iframe.html')






        

       

        

    
        

    



    
    
        



    





