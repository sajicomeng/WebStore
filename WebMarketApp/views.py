from django.shortcuts import render
from WebMarketApp.models import Customer
from django.http import HttpResponse
from django.views.generic import (ListView , FormView, CreateView)
from django.template import loader
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm
from .models import Customer
from django.contrib.auth import login, authenticate

class CustomerSignUpView(FormView):
    template_name = 'WebMarketApp/customer_signup.html'
    form_class = CustomerForm
    success_url = '/index/'
    model = Customer

    #queryset = Customer.objects.all()

def crudops(request):
    # Creating an entry

    customer = Customer(
        password="www.polo.com", mail="sorex@polo.com",
        username="sorex", phonenumber="002376970"
    )

    customer.save()

    # Read ALL entries
    objects = Customer.objects.all()
    res = 'Printing all Customer entries in the DB : <br>'

    for elt in objects:
        res += elt.username + "<br>"

    return HttpResponse(res)

def index(request):
    latest_customer_list = Customer.objects.order_by('mail')
    template = loader.get_template('WebMarketApp/index.html')
    context = {
        'customer_list': latest_customer_list,
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('WebMarketApp/SignUp.html')
    context = {
        'customer_list': ''
    }
    return HttpResponse(template.render(context, request))

def signup_submit(request):
    customer = Customer(
        password=request.POST['password'], mail=request.POST['email'],
        username=request.POST['firstname'], phonenumber="002376970"
    )
    try:
        customer.save()
        template = loader.get_template('WebMarketApp/MainTemplate.html')
        context = {
            'customer_list': ''
        }
        return HttpResponse(template.render(context, request))
    except IntegrityError as e:
        template = loader.get_template('WebMarketApp/SignUp.html')
        context = {
            'username_err': 'This username is used. Please choose another username!'
        }
        return HttpResponse(template.render(context, request))

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(response, "WebMarketApp/register.html", {"form":form})

class CustomerView(ListView):
    model = Customer

