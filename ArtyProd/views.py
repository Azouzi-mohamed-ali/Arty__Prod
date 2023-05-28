from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.conf import settings
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError
# Create your views here.

def index(request):
    med={
        'projects':Project.objects.all(),
        'Services':Service.objects.all(),
        
    }

    if request.user.is_authenticated:

        username = request.user.username
        med['username'] = username
    return render(request,'index.html ',med)


def Team(request):
    t={
        'personel':Personel.objects.all(),

    }
    return render(request,'team.html',t)
#def logout_view(request):
    logout(request)
    return redirect('index')

def contact(request):

    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()


    return render(request,'contact.html')



#def index(request):
    db = {
        'Pers': Personel.objects.all(),
        'Partenaire': Partenaire.objects.all(),
        'service': Service.objects.all(),
        'Project': Project.objects.all(),
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new Contact object and save it to the database
        contact = Contact(name=name, phone=phone, email=email,
                          subject=subject, message=message)
        contact.save()
        send_mail(
            subject,
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False
        )
        # messages.success(request,"message send succsufly")

    if request.user.is_authenticated:
        # if the user is authenticated, pass their username to the template
        username = request.user.username
        db['username'] = username

    return render(request, 'index.html', db)


def project_detail(request ):
    project1 =Project.objects.all()
    context = {'project1': project1}

    return render(request, 'project_detail.html', context)

def demande_detail(request, demande_id):
    demande = get_object_or_404(Demande, pk=demande_id)
    return render(request, 'demande_detail.html', {'demande': demande})

def projets (request):
    m={ 'demandes':Demande.objects.all(),

    }
    return render(request,'projets.html' ,m)

def demande_project(request):
    context = {}
    if request.method == 'POST':
        # Extract the relevant data from the POST request
        client_name = request.POST.get('client-name')
        number = request.POST.get('client-number')
        libelle = request.POST.get('libelle')
        image = request.FILES.POST.get('image')
        description = request.POST.get('description')

        # Create the new project object and save it to the database
        project = Project(client_name=client_name, number_client=number,
                          libelle=libelle, image=image, description=description)
        project.save()

        # Redirect the user to the project detail page for the new project
        return redirect('project_detail', project_id=project.id)

    if request.user.is_authenticated:
        # if the user is authenticated, pass their username to the template
        username = request.user.username
        context['username'] = username
    return render(request, 'demande.html', context)

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'sign-in.html')
    else:
        return render(request, 'sign-in.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = username
            user.save()
            authenticated_user = authenticate(request, username=username, password=password)
            login(request, authenticated_user)
            return redirect('index')
        except IntegrityError:
            error_message = "Username already exists. Please choose a different username."
            return render(request, 'sign-up.html', {'error_message': error_message})

    return render(request, 'sign-up.html')


def logout_view(request):
    logout(request)
    return redirect('index')

def create_demande(request):
    if request.method == 'POST':
        client_name = request.POST.get('name')
        number_client = request.POST.get('number_client')
        Type = request.POST.get('type')
        description = request.POST.get('message')

        demande = Demande(client_name=client_name, number_client=number_client, Type=Type, description=description)
        demande.save()

        return redirect('index')

    return render(request, 'demande.html')
   






def my_projects(request):
    projects = Project.objects.filter(client_name=request.user.username)
    context = {'projects': projects}
    if request.user.is_authenticated:
        # if the user is authenticated, pass their username to the template
        username = request.user.username
        context['username'] = username
    return render(request, 'my_projects.html', context)
