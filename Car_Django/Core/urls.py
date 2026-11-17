"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from App.views import (
    index_view,
    brand_list_view, add_brand_view, edit_brand_view, delete_brand_view,
    model_list_view, add_model_view, edit_model_view, delete_model_view,
    specification_list_view, add_specification_view, edit_specification_view, delete_specification_view,
    car_list_view, add_car_view, edit_car_view, delete_car_view,
    customer_list_view, add_customer_view, edit_customer_view, delete_customer_view,
    employee_list_view, add_employee_view, edit_employee_view, delete_employee_view,
    sale_list_view, add_sale_view, edit_sale_view, delete_sale_view,
    payment_list_view, add_payment_view, edit_payment_view, delete_payment_view,
    check_service_view, sign_up_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view, name='index_page'),
    #Brand
    path('brand/', brand_list_view, name='brand_list_page'),
    path('add_brand/', add_brand_view, name='add_brand_page'),
    path('edit_brand/<int:brand_id>/', edit_brand_view, name='edit_brand_page'),
    path('delete_brand/<int:brand_id>/', delete_brand_view, name='delete_brand_page'),

    #Model
    path('model/', model_list_view, name='model_list_page'),
    path('add_model/', add_model_view, name='add_model_page'),
    path('edit_model/<int:model_id>/', edit_model_view, name='edit_model_page'),
    path('delete_model/<int:model_id>/', delete_model_view, name='delete_model_page'),

    #Specification
    path('specification/', specification_list_view, name='specification_list_page'),
    path('add_specification/', add_specification_view, name='add_specification_page'),
    path('edit_specification/<int:specification_id>/', edit_specification_view, name='edit_specification_page'),
    path('delete_specification/<int:specification_id>/', delete_specification_view, name="delete_specification_page"),

    #Car
    path('car/', car_list_view, name='car_list_page'),
    path('add_car/', add_car_view, name='add_car_page'),
    path('edit_car/<int:car_id>/', edit_car_view, name='edit_car_page'),
    path('delete_car/<int:car_id>/', delete_car_view, name="delete_car_page"),

    #Customer
    path('customer/', customer_list_view, name='customer_list_page'),
    path('add_customer/', add_customer_view, name='add_customer_page'),
    path('edit_customer/<int:customer_id>/', edit_customer_view, name='edit_customer_page'),
    path('delete_customer/<int:customer_id>/', delete_customer_view, name="delete_customer_page"),

    #Employee
    path('employee/', employee_list_view, name='employee_list_page'),
    path('add_employee/', add_employee_view, name='add_employee_page'),
    path('edit_employee/<int:employee_id>/', edit_employee_view, name='edit_employee_page'),
    path('delete_employee/<int:employee_id>/', delete_employee_view, name="delete_employee_page"),

    #Sale
    path('sale/', sale_list_view, name='sale_list_page'),
    path('add_sale/', add_sale_view, name='add_sale_page'),
    path('edit_sale/<int:sale_id>/', edit_sale_view, name='edit_sale_page'),
    path('delete_sale/<int:sale_id>/', delete_sale_view, name="delete_sale_page"),

    #Payment
    path('payment/', payment_list_view, name='payment_list_page'),
    path('add_payment/', add_payment_view, name='add_payment_page'),
    path('edit_payment/<int:payment_id>/', edit_payment_view, name='edit_payment_page'),
    path('delete_payment/<int:payment_id>/', delete_payment_view, name="delete_payment_page"),

    #Car service check
    path('check_service/', check_service_view, name='check_service_page'),

    # Authentication
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),

]
