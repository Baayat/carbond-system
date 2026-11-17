from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Brand, Model, Specification, Car, Customer, Employee, Sale, Payment
from .forms import BrandForm, ModelForm, SpecificationForm, CarForm, CustomerForm, EmployeeForm, SaleForm, PaymentForm, CheckServiceForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#Index view
@login_required
def index_view(req):
    return render(req, 'index.html')

#List view,
#Brand-list
@login_required
def brand_list_view(req):
    brands = Brand.objects.all()
    return render(req, 'brand_list.html', {'brands': brands})

#Model-list
@login_required
def model_list_view(req):
    models = Model.objects.select_related('brand').all()
    return render(req, 'model_list.html', {'models': models})

#Specification-list
@login_required
def specification_list_view(req):
    specifications = Specification.objects.all()
    return render(req, 'specification_list.html', {'specifications':specifications})

#Car-list
@login_required
def car_list_view(req):
    cars = Car.objects.all()
    return render(req, 'car_list.html', {'cars':cars})

#Customer-list
@login_required
def customer_list_view(req):
    customers = Customer.objects.all()
    return render(req, 'customer_list.html', {'customers':customers})

#Employee-list
@login_required
def employee_list_view(req):
    employees = Employee.objects.all()
    return render(req, 'employee_list.html', {'employees':employees})

#Sale-list
@login_required
def sale_list_view(req):
    sales = Sale.objects.select_related('car', 'employee', 'customer').all()
    return render(req, 'sale_list.html', {'sales':sales})

#Payment-list
@login_required
def payment_list_view(req):
    payments = Payment.objects.select_related('sale').all()
    return render(req, 'payment_list.html', {'payments':payments})

#Add view (create + read in one page)
#Brand-Read
@login_required
def add_brand_view(req):
    message = None
    if req.method == "POST":
        brand_form = BrandForm(req.POST)
        if brand_form.is_valid():
            brand_form.save()
            message = "Brand Added Successfully"
            brand_form = BrandForm()
    else:
        brand_form = BrandForm()

    brands = Brand.objects.all()
    context = {'form': brand_form, 'msg': message, 'brands': brands}
    return render(req, "add_brand.html", context)

#Model-Read
@login_required
def add_model_view(req):
    message = None
    if req.method == "POST":
        model_form = ModelForm(req.POST)
        if model_form.is_valid():
            model_form.save()
            message = "Model Added Successfully"
            model_form = ModelForm()
    else:
        model_form = ModelForm()

    models = Model.objects.select_related('brand').all()
    context = {'form': model_form, 'msg': message, 'models': models}
    return render(req, "add_model.html", context)

#Specification-Read
@login_required
def add_specification_view(req):
    message = None
    if req.method == "POST":
        specification_form = SpecificationForm(req.POST)
        if specification_form.is_valid():
            specification_form.save()
            message = "Specification Added Successfully"
            specification_form = SpecificationForm()
    else:
        specification_form = SpecificationForm()

    specifications = Specification.objects.all()
    context = {'form': specification_form,
    'msg':message, 'specifications':specifications}
    return render(req, "add_specification.html", context)

#Car-Read
@login_required
def add_car_view(req):
    message = None
    if req.method == "POST":
        car_form = CarForm(req.POST)
        if car_form.is_valid():
            car_form.save()
            message = "Car Added Successfully"
            car_form = CarForm()
    else:
        car_form = CarForm()

    cars = Car.objects.all()
    context = {'form': car_form,
    'msg':message, 'cars':cars}
    return render(req, "add_car.html", context)

#Customer-Read
@login_required
def add_customer_view(req):
    message = None
    if req.method == "POST":
        customer_form = CustomerForm(req.POST)
        if customer_form.is_valid():
            customer_form.save()
            message = "Customer Added Successfully"
            customer_form = CustomerForm()
    else:
        customer_form = CustomerForm()

    customers = Customer.objects.all()
    context = {'form': customer_form,
    'msg':message, 'customers':customers}
    return render(req, "add_customer.html", context)

#Employee-Read
@login_required
def add_employee_view(req):
    message = None
    if req.method == "POST":
        employee_form = EmployeeForm(req.POST)
        if employee_form.is_valid():
            employee_form.save()
            message = "Employee Added Successfully"
            employee_form = EmployeeForm()
    else:
        employee_form = EmployeeForm()

    employees = Employee.objects.all()
    context = {'form': employee_form,
    'msg':message, 'employees':employees}
    return render(req, "add_employee.html", context)

#Sale-Read
@login_required
def add_sale_view(req):
    message = None
    if req.method == "POST":
        sale_form = SaleForm(req.POST)
        if sale_form.is_valid():
            sale_form.save()
            message = "Sale Added Successfully"
            sale_form = SaleForm()
    else:
        sale_form = SaleForm()

    sales = Sale.objects.select_related('car', 'employee', 'customer').all()
    context = {'form': sale_form,
    'msg':message, 'sales':sales}
    return render(req, "add_sale.html", context)

#Payment-Read
@login_required
def add_payment_view(req):
    message = None
    if req.method == "POST":
        payment_form = PaymentForm(req.POST)
        if payment_form.is_valid():
            payment_form.save()
            message = "Payment Added Successfully"
            payment_form = PaymentForm()
    else:
        payment_form = PaymentForm()

    payments = Payment.objects.select_related('sale').all()
    context = {'form': payment_form,
    'msg':message, 'payments':payments}
    return render(req, "add_payment.html", context)

# Edit view (Update)
#Brand-Edit
@login_required
def edit_brand_view(req, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if req.method == "POST":
        brand_form = BrandForm(req.POST, instance=brand)
        if brand_form.is_valid():
            brand_form.save()
            message = "Changes saved Successfully!"
        else:
            message = "Form has Invalid data"
    else:
        brand_form = BrandForm(instance=brand)
        message = None

    context = {'form': brand_form, 'brand': brand, 'msg': message}
    return render(req, "edit_brand.html", context)

#Model-Edit
@login_required
def edit_model_view(req, model_id):
    model = get_object_or_404(Model, id=model_id)
    if req.method == "POST":
        model_form = ModelForm(req.POST, instance=model)
        if model_form.is_valid():
            model_form.save()
            message = "Changes saved Successfully!"
        else:
            message = "Form has Invalid data"
    else:
        model_form = ModelForm(instance=model)
        message = None

    context = {'form': model_form, 'model': model, 'msg': message}
    return render(req, "edit_model.html", context)

#Specification-Edit
@login_required
def edit_specification_view(req, specification_id):
    specification = get_object_or_404(Specification, id=specification_id)
    message = None
    if req.method == "POST":
        specification_form = SpecificationForm(req.POST, instance=specification)
        if specification_form.is_valid():
            specification_form.save()
            message = "Changes saved Successfully!"
        else:
            message = "Form has Invalid data"
    else:
        specification_form = SpecificationForm(instance=specification)

    context = {'form': specification_form, 'specification': specification, 'msg': message}
    return render(req, "edit_specification.html", context)

#Car-Edit
@login_required
def edit_car_view(req, car_id):
    car = get_object_or_404(Car, id=car_id)
    message = None
    if req.method == "POST":
        car_form = CarForm(req.POST, instance=car)
        if car_form.is_valid():
            car_form.save()
            message = "Changes saved Successfully!"
        else:
            message = "Form has Invalid data"
    else:
        car_form = CarForm(instance=car)

    context = {'form': car_form, 'car': car, 'msg': message}
    return render(req, "edit_car.html", context)

#Customer-Edit
@login_required
def edit_customer_view(req, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    message = None
    if req.method == "POST":
        customer_form = CustomerForm(req.POST, instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            message = "Changes saved Successfully!"
        else:
            message = "Form has Invalid data"
    else:
        customer_form = CustomerForm(instance=customer)

    context = {'form': customer_form, 'customer': customer, 'msg': message}
    return render(req, "edit_customer.html", context)

#Employee-Edit
@login_required
def edit_employee_view(req, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    message = None
    if req.method == "POST":
        employee_form = EmployeeForm(req.POST, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            message = "Changes saved Successfully!"
        else:
            message = "Form has Invalid data"
    else:
        employee_form = EmployeeForm(instance=employee)

    context = {'form': employee_form, 'employee': employee, 'msg': message}
    return render(req, "edit_employee.html", context)

#Sale-Edit
@login_required
def edit_sale_view(req, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    message = None
    if req.method == "POST":
        sale_form = SaleForm(req.POST, instance=sale)
        if sale_form.is_valid():
            sale_form.save()
            message = "Changes saved Successfully!"
        else:
            message = "Form has Invalid data"
    else:
        sale_form = SaleForm(instance=sale)

    context = {'form': sale_form, 'sale': sale, 'msg': message}
    return render(req, "edit_sale.html", context)

#Payment-Edit
@login_required
def edit_payment_view(req, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    message = None
    if req.method == "POST":
        payment_form = PaymentForm(req.POST, instance=payment)
        if payment_form.is_valid():
            payment_form.save()
            message = "Changes saved Successfully!"
        else:
            message = "Form has Invalid data"
    else:
        payment_form = PaymentForm(instance=payment)

    context = {'form': payment_form, 'payment': payment, 'msg': message}
    return render(req, "edit_payment.html", context)

#Delete view
#Brand-Delete
@login_required
def delete_brand_view(req, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    brand.delete()
    return HttpResponseRedirect('/add_brand/')

#Model-Delete
@login_required
def delete_model_view(req, model_id):
    model = get_object_or_404(Model, id=model_id)
    model.delete()
    return HttpResponseRedirect('/add_model/')

#Specification-Delete
@login_required
def delete_specification_view(req, specification_id):
    specification = get_object_or_404(Specification, id=specification_id)
    specification.delete()
    return HttpResponseRedirect('/add_specification/')

#Car-Delete
@login_required
def delete_car_view(req, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return HttpResponseRedirect('/add_car/')

#Customer-Delete
@login_required
def delete_customer_view(req, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return HttpResponseRedirect('/add_customer/')

#Employee-Delete
@login_required
def delete_employee_view(req, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return HttpResponseRedirect('/add_employee/')

#Sale-Delete
@login_required
def delete_sale_view(req, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    sale.delete()
    return HttpResponseRedirect('/add_sale/')

#Payment-Delete
@login_required
def delete_payment_view(req, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.delete()
    return HttpResponseRedirect('/add_payment/')

#Car-Check service (based on get_service() in car.py)
@login_required
def check_service_view(req):
    result = None
    if req.method == "POST":
        service_form = CheckServiceForm(req.POST)
        if service_form.is_valid():
            car = service_form.cleaned_data['car']
            current = service_form.cleaned_data['current_mileage']
            last = service_form.cleaned_data['last_service_mileage']
            result = {
                'car': car,
                'since_service': current - last,
                'interval': car.service_interval,
                'due': car.get_service(current, last),
            }
    else:
        service_form = CheckServiceForm()

    context = {'form': service_form, 'result': result}
    return render(req, "check_service.html", context)

# Sign up view
def sign_up_view(req):
    if req.method == "POST":
        sign_up_form = UserCreationForm(req.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        sign_up_form = UserCreationForm()

    context = {'form': sign_up_form}
    return render(req, "registration/sign_up.html", context)
