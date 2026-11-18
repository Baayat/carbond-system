from django.contrib import admin
from .models import Brand, Model, Specification, Car, Customer, Employee, Sale, Payment

# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand_name",)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ( "brand", "year", "model_name")


class SpecificationAdmin(admin.ModelAdmin):
    list_display = ("car_specification", "value","car")
admin.site.register(Specification, SpecificationAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "color", "status", "mileage", "price","car_type", "engine_type", "capacity")
admin.site.register(Car, CarAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "contact", "address", "gender")
admin.site.register(Customer, CustomerAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "contact", "role", "gender", "birth_year", "hire_date")
admin.site.register(Employee, EmployeeAdmin)

class SaleAdmin(admin.ModelAdmin):
    list_display = ("sale_price", "total_paid", "car", "employee", "customer")
admin.site.register(Sale, SaleAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_date", "amount", "payment_method", "sale")
admin.site.register(Payment, PaymentAdmin)
