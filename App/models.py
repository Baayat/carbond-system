from datetime import date
from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    model_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand.brand_name} {self.model_name} ({self.year})"


class Car(models.Model):
    TYPE_OPTIONS = [
        ('S','SUV'),
        ('H','Hatchback'),
        ('P','Pickup')
    ]
    STATUS_OPTIONS = [
        ('A','Available'),
        ('S','Sold'),
        ('R','Reserved')
    ]
    ENGINE_TYPE=[
        ('E','Electric'),
        ('H','Hybrid'),
        ('D','Diesel'),
        ('P','Petrol')
    ]
    # Service interval (km) by body type for the current Car model.
    SERVICE_INTERVALS = {'S': 10000, 'H': 10000, 'P': 15000}

    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    status = models.CharField(max_length=2, choices=STATUS_OPTIONS)
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    car_type = models.CharField(max_length=2, choices=TYPE_OPTIONS)
    engine_type = models.CharField(max_length=30,choices=ENGINE_TYPE)
    capacity = models.PositiveIntegerField(help_text="Number of seats")

    @property
    def service_interval(self):
        return self.SERVICE_INTERVALS.get(self.car_type, 10000)

    @property
    def battery_tank_display(self):
        return "—"

    def get_service(self, current_mileage, last_service_mileage):
        """Service is due when the mileage since the last service reaches the car's interval."""
        return (current_mileage - last_service_mileage) >= self.service_interval

    def __str__(self):
        return f"{self.model} ({self.color})"

class Specification(models.Model):
    car_specification = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car_specification}: {self.value}"


class Customer(models.Model):
    GENDER_OPTIONS = [
        ('M','Male'),
        ('F','Female')
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employee(models.Model):
    GENDER_OPTIONS = [
        ('M','Male'),
        ('F','Female')
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    role = models.CharField(max_length=30)
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    birth_year = models.PositiveIntegerField(help_text="Used to calculate age")
    hire_date = models.DateField(auto_now=False)

    @property
    def age(self):
        return date.today().year - self.birth_year

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Sale(models.Model):
    sale_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sale {self.id} - {self.car} ({self.customer})"

class Payment(models.Model):
    METHOD_OPTIONS = [
        ('credit_card','Credit Card'),
        ('cash','Cash'),
        ('mobile_money','Mobile Money'),
        ('bank_transfer','Bank Transfer'),
    ]
    payment_date = models.DateField(auto_now=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=METHOD_OPTIONS)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

    @property
    def balance(self):
        # Balance = sale price of the sale - amount of the payment (get_balance)
        return self.sale.sale_price - self.amount

    def __str__(self):
        return f"{self.id}-UGX {self.amount}({self.sale})"
