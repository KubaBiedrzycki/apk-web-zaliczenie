from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from .models import Car, Client, Rental, Condition
from .forms import CarForm, ClientForm


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
    query = request.GET.get('q')
    cars = Car.objects.all()

    if query:
        cars = cars.filter(brand__icontains=query) | cars.filter(model__icontains=query)

    # Obsługa formularza dodawania nowego samochodu
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')  # Odśwież stronę po dodaniu samochodu
    else:
        form = CarForm()

    return render(request, 'carrent/car/list.html', {'cars': cars, 'query': query, 'form': form})

def client_list(request):
    query = request.GET.get('q')
    clients = Client.objects.all()

    if query:
        clients = clients.filter(firstname__icontains=query) | clients.filter(lastname__icontains=query)

    # Obsługa formularza dodawania nowego samochodu
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Odśwież stronę po dodaniu samochodu
    else:
        form = ClientForm()

    return render(request, 'carrent/client/list.html', {'clients': clients, 'query': query, 'form': form})

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