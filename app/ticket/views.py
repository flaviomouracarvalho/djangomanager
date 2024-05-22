from django.shortcuts import render, redirect
from ticket.models import Ticket

def home(request):
    tickets = Ticket.objects.all()
    count = Ticket.objects.count_closed_and_opened()
    return render(request, "home.html", {"tickets":tickets, "count": count})

def close_tickets_by_ids(request):
    if ids := request.POST.get("tickets"):
        tickets_to_close = ids.split(",")
        #Ticket.objects.filter(id__in=tickets_to_close).close()
        Ticket.objects.close_tickets(tickets_to_close)
    return redirect("home")

def open_tickets_by_ids(request):
    if ids := request.POST.get("tickets"):
        tickets_to_open = ids.split(",")
        #Ticket.objects.filter(id__in=tickets_to_open).open()
        Ticket.objects.open_tickets(tickets_to_open)
    return redirect("home")

def close_all_tickets(request):
    Ticket.objects.all().close()
    return redirect("home")

def open_all_tickets(request):
    Ticket.objects.all().open()
    return redirect("home")