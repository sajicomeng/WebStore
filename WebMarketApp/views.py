from django.shortcuts import render
from WebMarketApp.models import Customer
from django.http import HttpResponse
from django.views.generic import ListView
from django.template import loader

# Create your views here.
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

    # Read a specific entry:
    # sorex = Customer.objects.get(username="sorex")
    # res += 'Printing One entry <br>'
    # res += sorex.username
    #
    # # Delete an entry
    # res += '<br> Deleting an entry <br>'
    # sorex.delete()
    #
    # # Update
    # customer = Customer(
    #     password="www.polo.com", mail="sorex@polo.com",
    #     username="sorex", phonenumber="002376970"
    # )
    #
    # customer.save()
    # res += 'Updating entry<br>'
    #
    # customer = Customer.objects.get(username='sorex')
    # customer.username = 'thierry'
    # customer.save()

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

class CustomerView(ListView):
    model = Customer

