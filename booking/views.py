from django.shortcuts import render, redirect
from .models import BookingDetail, Payment
# Create your views here.

def booking(request):
    
    name = request.POST['destination_name']
    price = request.POST['destination_price']
    username = request.POST['username']

    details = BookingDetail.objects.create(name=name, price=price, username=username)
    details.save()

    packname = BookingDetail.objects.get(username__exact=username)
    
    return render(request,"booking.html", {'packname':packname})

def book(request):
    
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    price = request.POST['price']
    numticket = request.POST['numticket']
    cardnumber = request.POST['cardnumber']

    paydetails = Payment.objects.create(first_name=firstname, last_name=lastname, email=email, price=price, numticket=numticket, cardnumber=cardnumber)
    paydetails.save()
    return render(request,'payment.html')