from django.contrib.auth.models import User
from django.http import request
from django.http.response import HttpResponseNotAllowed
from django.contrib.auth.forms import AuthenticationForm
from registration.models import student
from django.shortcuts import redirect, render, resolve_url
from . import forms
from .models import Application, Department, Student 
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')


def apply(request):
    if request.method == 'POST':
        form = forms.Apply(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration:sent')
    else:
        form = forms.Apply()

    form = forms.Apply()
    return render(request, 'register.html', {'form': form})


def sent(request):
    return render(request, 'sent.html')

@login_required(login_url='/login/')
def dashboard(request):
    nbr_approved = Application.objects.filter(status='APPROVED').count()
    nbr_pending = Application.objects.filter(status='PENDING').count()
    return render(request, 'applications.html', {'nbr_approved': nbr_approved, 'nbr_pending': nbr_pending})


def approved(request):
    applications = Application.objects.filter(status='APPROVED')
    return render(request, 'approved.html', {'applications': applications})

def pending(request):
    applications = Application.objects.filter(status='PENDING')
    return render(request, 'pending.html', {'applications': applications})


def approve(request):
    if request.method == 'POST':
        application = Application.objects.get(id=request.POST.get('id'))
        application.status = "APPROVED"
        application.save()
        user = User()
        user.username = application.email
        password = User.objects.make_random_password()
        print(password)
        user.set_password(password)
        user.save()
        student = Student()
        student.application = application
        student.user = user
        student.save()
        return redirect(resolve_url('registration:pending'))
    return HttpResponseNotAllowed()


def delete(request):
    if request.method == 'POST':
        application = Application.objects.get(id=request.POST.get('id'))
        application.status = "DELETED"
        application.save()
        return redirect(resolve_url('registration:pending'))
    return HttpResponseNotAllowed()

def create_student(request):
    if request.method == 'POST':
        application = Application.objects.get(id=request.POST.get('id'))
        application.status = "APPROVED"
        application.save()
        user = User()
        user.username = application.email
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save()
        student = Student()
        student.application = application
        student.user = user
        student.save()
        return redirect(resolve_url('registration:pending'))
    return HttpResponseNotAllowed()

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser == True:
                return redirect('registration:dashboard')
            else:
                return redirect('registration:student_page')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(resolve_url('registration:login'))

@login_required(login_url='/login/')
def change_department(request):
    if request.method == 'POST':
        user = request.user
        student = Student.objects.get(user_id = user.id)
        application = Application.objects.get(id = student.application_id)
        application.department_id = request.POST.get('id')
        application.save()
        return redirect(resolve_url('registration:student_page'))

    else:
        return render(request,'registration:login')

@login_required(login_url='/login/')
def student_page(request):
    
    departments = Department.objects.all()
    student = Application.objects.get(email = request.user.username)
    dep_id = student.department_id
    current_dep = Department.objects.get(id = dep_id)
    return render(request,'student_page.html', context={'student': student, 'departments':departments, 'current_dep': current_dep})


    