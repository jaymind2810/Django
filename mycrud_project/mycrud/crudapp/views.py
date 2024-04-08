from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RegistrationForm


def home(request):
    return render(request, 'index.html')

def add_registration(request):

    if request.method == 'POST':
        print("Herrrrrr")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        print(first_name, "----_First Name --------")

        if first_name != "" and last_name != "" and email != "" :
            b = RegistrationForm(first_name=first_name, last_name=last_name, email=email, mobile=mobile, city=city, address=address, gender=gender)
            b.save()
            return redirect('registration_list')

    return render(request, 'add_registration.html')

def registration_list(request):

    regi_list = RegistrationForm.objects.all()

    return render(request, 'registration_list.html', {'regi_list': regi_list})