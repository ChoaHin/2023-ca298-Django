from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

def index(request):
    return render(request, 'index.html')

def create_pizza(request):
    if request.method == "POST":
        # create a new copy of the form with the data the user 
				# entered , it is stored in request.POST
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False) # create the Employee object and don't save it yet
			## other steps go here possibilities include
			# creating other objects
		  	# editing attributes of employee
            pizza.save() # finally save the employee object
            return redirect('detail', pizza.id)
        else:
						# form has errors
						# send the form back to the user
            return render(request, 'create_pizza.html', {'form': form})
    else:
        # normal get reuqest, user wants to see the form 
        form = PizzaForm()
        return render(request, 'create_pizza.html', {'form': form})

def detail(request, pizzaid):
    pizza = Pizza.objects.get(id=pizzaid)
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            pizza.owned_by = customer
            pizza.save()
            return redirect('final', customer.id)
        else:
           return render(request, 'detail.html', {'form': form, 'detail': pizza})
    else:
        form = DetailForm()
        return render(request, 'detail.html', {'form': form, 'detail': pizza})

def final(request, custid):
    customer = Customer.objects.get(id=custid)
    pizza = Pizza.objects.get(owned_by=custid)
    toppings = eval(pizza.topping)
    return render(request, 'final.html', {'customer': customer, 'pizza': pizza, 'toppings': toppings})
