from .models import Traveller
from django.shortcuts import redirect, render


def index_page(request):
    data = Traveller.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def homepage(request):
    return render(request, "Home Page.html")


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
        payment = request.POST.get('payment')

        query = Traveller(name=name, email=email, phone=phone, origin=origin, destination=destination,
                          payment=payment)
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
        payment = request.POST.get('payment')

        update_info = Traveller.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.phone = phone
        update_info.origin = origin
        update_info.destination = destination
        update_info.payment = payment

        update_info.save()
        return redirect("/")

    d = Traveller.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
