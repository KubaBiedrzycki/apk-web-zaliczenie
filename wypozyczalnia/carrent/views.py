from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from .models import Car, Client, Rental, Condition

# Create your views here.

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Carrental - wypożycz swój wymarzony samochód! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def home(request):
    return render(request, 'carrent/home.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'carrent/car/list.html', {'cars': cars})

def client_list(request):
    if request.method == 'POST':
        cars = Client.objects.filter(firstname__icontains=request.POST['phrase'])
    else:
        # pobieramy wszystkie obiekty Person z bazy poprzez QuerySet
        clients = Client.objects.all()

    return render(request,
                  "carrent/client/list.html",
                  {'clients': clients})

def rental_list(request):
    if request.method == 'POST':
        rentals = Rental.objects.filter(untill__icontains=request.POST['phrase'])
    else:
        # pobieramy wszystkie obiekty Person z bazy poprzez QuerySet
        rentals = Rental.objects.all()

    return render(request,
                  "carrent/rental/list.html",
                  {'rentals': rentals})

def condition_list(request):
    if request.method == 'POST':
        conditions = Condition.objects.filter(tires__icontains=request.POST['phrase'])
    else:
        # pobieramy wszystkie obiekty Person z bazy poprzez QuerySet
        conditions = Condition.objects.all()

    return render(request,
                  "carrent/condition/list.html",
                  {'conditions': conditions})

def condition_detail(request, pk):
    condition = get_object_or_404(Condition, pk=pk)
    return render(request, 'carrent/condition/detail.html', {'condition': condition})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'carrent/client/detail.html', {'client': client})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'carrent/car/detail.html', {'car': car})

def rental_detail(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    return render(request, 'carrent/rental/detail.html', {'rental': rental})