# -*- coding: utf-8 -*-

"""
In the views script you define the view functions.

In these functions you decide what html template to use and what data you send
to them as dictionaries.
"""

#############
# Libraries #
#############

from django.shortcuts import render
from .models import Project


##################
# View functions #
##################

def home(request):
    """
    Home function. Just show the home page.

    Get all the objects of class 'Project' and send them to the template
    portfolio/templates/home.html

    Args:
        request (WSGIRequest): This is a subclass of python's
            http.server.BaseHTTPRequestHandler. It represents an incoming http
            request from a client.

    Returns:
        HttpResponse with arguments containing all the info to render the web
            page.
    """

    # See that the path is relative to ./templates
    return render(request, 'home.html')


def all_projects(request):
    """
    Portfolio-app home function

    Get all the objects of class 'Project' and send them to the template
    portfolio/templates/home.html

    Args:
        request (WSGIRequest): This is a subclass of python's
            http.server.BaseHTTPRequestHandler. It represents an incoming http
            request from a client.

    Returns:
        HttpResponse with arguments containing all the info to render the web
            page.
    """

    # Get all the projects objects
    projects = Project.objects.all()

    # See that the path is relative to ./templates
    return render(request, 'all_projects.html', {'projects': projects})