from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact.html', views.contact, name = 'contact'),
    path('services.html', views.service, name = 'service'),
    path('about.html', views.about, name = 'about'),
    path('gallery.html', views.gallery, name = 'gallery'),
]