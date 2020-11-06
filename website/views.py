from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # send an email
        send_mail(
            email , #subject
            message , #message
            email , #from email
            ['mihailomaric001@gmail.com'], #to email
        )

        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'services.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def shop(request):
    return render(request, 'base.html', {})