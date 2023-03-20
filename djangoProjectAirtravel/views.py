from .models import Traveller
from django.shortcuts import redirect, render


def index_page(request):
    data = Traveller.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def homepage(request):
    return render(request, "Home Page.html")


def bookingservice(request):
    return render(request, "Booking Service.html")


def edit_page(request):
    return render(request, "edit.html")


def deleteData(request, id):
    d = Traveller.objects.get(id=id)
    d.delete()
    return redirect('index')
    return render(request, "index.html")


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        seat = request.POST.get('seat')
        id_number = request.POST.get('id number')
        amount = request.POST.get('amount')

        query = Traveller(name=name, email=email, phone=phone, origin=origin, destination=destination,
                          seat=seat, id_number=id_number, amount=amount)
        query.save()
        return redirect('index')
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        seat = request.POST.get('seat')
        id_number = request.POST.get('id number')
        amount = request.POST.get('amount')

        update_info = Traveller.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.phone = phone
        update_info.origin = origin
        update_info.destination = destination
        update_info.seat = seat
        update_info.id_number = id_number
        update_info.amount = amount

        update_info.save()
        return redirect("index")

    d = Traveller.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
