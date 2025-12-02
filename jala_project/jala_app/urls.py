from django.urls import path
from jala_app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('base/',views.base,name='base'),
    path('employee_form_page',views.employee_form_page,name='employee_form'),
    path('employee_search_page/', views.employee_search_page, name='employee_search'),
    path('update_employee/<int:id>/',views.update_employee,name='update_employee'),
    path('multiple_tabs',views.multipletabs,name='multiple_tabs'),
    path('menu',views.menu,name='menu'),
    path('autocomplete',views.autocomplete,name='autocomplete'),
    path('collapse',views.collapse,name='collapse'),
    path('image',views.image,name='image'),
    path('slider',views.slider,name='slider'),
    path('tooltip',views.tooltip,name='tooltip'),
    path('popup',views.popup,name='popup'),
    path('links',views.links,name='links'),
    path('css',views.css,name='css'),
    path('iframe',views.iframe,name='iframe'),





        

]