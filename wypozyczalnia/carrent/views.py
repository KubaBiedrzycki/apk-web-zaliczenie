from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Carrental - wypożycz swój wymarzony samochód! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)