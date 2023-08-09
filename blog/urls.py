"""
URL configuration for blog app

See that all urls defined in the local variable urlpatterns are supossed to
start with host:port/blog/

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.urls import path


# from app01 import views as app01_views

# Así importo de forma absoluta respecto a la carpeta de proyecto
# from blog import views as blog_views

# Así importo de forma relativa respecto a la ubicación de este script
# Esto sólo puede hacerse en un mismo package
from . import views as blog_views

# En todos los urls.py de cada aplicación conviene poner esta variable
# con el nombre de la aplicación. Esto se usa como referencia.
# Sí, importante, va en minúscula. Tiene que ser esa y no otra.
app_name = 'blog'

urlpatterns = [
    path('', blog_views.all_blogs, name='all_blogs'),
    # Para ver cualquier dirección con un entero .../blog/3/
    path('<int:blog_id>/', blog_views.blog_by_id, name='oneblog'),
]
