from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PatientForm
from .models import Addpatient

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
            user = form.cleaned_data_get('username')
            messages.success('Account Successfully Created for'+ user)
            
    context = {'form':form}
    return render(request, "register.html", context)


def login_page(request):
    if request.method=="POST":
        email= request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
                login(request, user)
                return redirect('index_page')
        else:
            messages.error(request, 'Wrong Spelt or email or Password')
            return redirect('login_page')
    else:       
        return render(request, "login_page.html")

def logout_page(request):
    logout(request)
    return redirect('login_page')

def index(request):
    return render(request,"index.html")

def upload(request):
    return render(request,"upload.html")

def patient_list(request):
    addpatient = Addpatient.objects.all()
    context = {'addpatient':addpatient}
    return render(request, "./patients details/patient-list.html", context)

def add_patient(request):
    addpatient = Addpatient.objects.all()
    form = PatientForm()
    if request.method=='POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-list')
    context = {'addpatient': addpatient, 'form': form}
    return render(request, "./patients details/add-patient.html", context)

def update_Patientlist(request, pk):
    addpatient = Addpatient.objects.get(id=pk)
    if request.method=='POST':
        form = PatientForm(request.POST, instance=addpatient)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, './patient details/update.html ')

def deleteTask(request, pk):
    item = Addpatient.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, './patient detail/delete.html', context)

def doctor(request):
    context = {}
    return render(request, "doctor.html", context)

def appointment(request):
    context = {}
    return render(request, "appointment.html", context) 

def contact(request):
    context = {}
    return render(request, "contact.html", context)

def inpatient(request):
    context = {}
    return render(request, "in-patient.html", context)

def outpatient(request):
    context = {}
    return render(request, "out-patient.html", context)