from django.contrib import admin 
from django.urls import path, include 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('cadastro/', include('cadastro.urls')),  # Inclui as URLs do app cadastro 
]