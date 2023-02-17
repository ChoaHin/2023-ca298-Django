from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse # import the jsonresponse object

# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books':all_books})

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    record = Record.objects.filter(book = bookid)
    return render(request, 'single_book.html', {'book':single_book, 'record':record})

def view_specific_year(request, year):
    specific_year = Book.objects.filter(year = year)
    return render(request, 'all_books.html', {'books':specific_year})

def view_specific_genre(request, genre):
    specific_genre = Book.objects.filter(genre__iexact=genre)
    return render(request, 'all_books.html', {'books':specific_genre})

def view_genre_year(request, genre, year):
    specific_genre_year = Book.objects.filter(genre__iexact=genre, year = year)
    return render(request,'all_books.html', {'books':specific_genre_year})

def show_customer(request, custid):
    cust = get_object_or_404(Customer, id=custid) # get a customer with id=1
    # extract a list of book ids from borrowings 
    # from Borrow where customer = cust
    record = Record.objects.filter(customer = custid)
    return render(request, 'customer.html', {'customer':cust, 'record':record}) 

# example for endpoint http://127.0.0.1:8000/example?variable1=a&variable2=b
# the two variables are variable1 and variable2, they are separated by "&"
def example(request):
	# Get the value for variable1, or use "x" if variable1 is not in the url
	variable1 = request.GET.get('variable1','x') 
	variable2 = request.GET.get('varaible2','y')

# assumes get parameters 
# num1 and num2(
# e.g. http://127.0.0.1:8000/add?num1=5&num2=6 returns 11
def api_add(request):
	# use 1 as default
	# we should enforce type restriction by casting the value passed to a float
	# they are assumed strings by default
	# see how to cast here: https://www.w3schools.com/python/python_casting.asp
	num1 = float(request.GET.get('num1',1)) 
	num2 = float(request.GET.get('num2',1))
	added = num1 + num2 # calculate the added value
	# prepare a dict to return as a json response
  # we have to give the value 'added' a key we will call 'result'
	resp_dict = {'result':added}
	return JsonResponse(resp_dict) # return the dict as a json respone

def api_subtract(request):
    num1 = float(request.GET.get('num1', 1))
    num2 = float(request.GET.get('num2', 1))
    subtracted = num1 - num2
    resp_dict = {'result':subtracted}
    return JsonResponse(resp_dict)

def api_divide(request):
    num1 = float(request.GET.get('num1', 1))
    num2 = float(request.GET.get('num2', 1))
    divided = num1 / num2
    resp_dict = {'result':divided}
    return JsonResponse(resp_dict)

def api_multiply(request):
    num1 = float(request.GET.get('num1', 1))
    num2 = float(request.GET.get('num2', 1))
    multiplied = num1 * num2
    resp_dict = {'result':multiplied}
    return JsonResponse(resp_dict)

def api_exponential(request):
    num1 = float(request.GET.get('num1', 1))
    num2 = float(request.GET.get('num2', 1))
    exponentialed = num1 ** num2
    resp_dict = {'result':exponentialed}
    return JsonResponse(resp_dict)