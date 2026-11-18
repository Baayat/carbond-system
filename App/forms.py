from django.forms import ModelForm as DjangoModelForm
from django import forms
from .models import Brand, Model, Specification, Car, Customer, Employee, Sale, Payment

class BrandForm(DjangoModelForm):
    class Meta:
        model = Brand
        fields = ("brand_name",)

class ModelForm(DjangoModelForm):
    class Meta:
        model = Model
        fields = ("brand", "year", "model_name")

class SpecificationForm(DjangoModelForm):
    class Meta:
        model = Specification
        fields = '__all__'

class CarForm(DjangoModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CustomerForm(DjangoModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class EmployeeForm(DjangoModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'hire_date':forms.DateInput(attrs={'type':'date'}),
        }

class SaleForm(DjangoModelForm):
    class Meta:
        model = Sale
        fields = '__all__'

class PaymentForm(DjangoModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'payment_date':forms.DateInput(attrs={'type':'date'}),
        }

class CheckServiceForm(forms.Form):
    car = forms.ModelChoiceField(queryset=Car.objects.all())
    current_mileage = forms.IntegerField(min_value=0)
    last_service_mileage = forms.IntegerField(min_value=0)

    def clean(self):
        cleaned = super().clean()
        current = cleaned.get('current_mileage')
        last = cleaned.get('last_service_mileage')
        if current is not None and last is not None and last > current:
            raise forms.ValidationError("Last service mileage cannot be greater than the current mileage.")
        return cleaned
