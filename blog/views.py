# -*- coding: utf-8 -*-

"""
In the views script you define the view functions.

In these functions you decide what html template to use and what data you send
to them as dictionaries.
"""

#############
# Libraries #
#############

from django.shortcuts import render, get_object_or_404
from .models import Blog


##################
# View functions #
##################

def all_blogs(request):
    """
    Blog-app home function

    Get all the objects of class 'Blog' and send them to the template
    blog/templates/all_blogs.html

    Args:
        request (WSGIRequest): This is a subclass of python's
            http.server.BaseHTTPRequestHandler. It represents an incoming http
            request from a client.

    Returns:
        HttpResponse with arguments containing all the info to render the web
            page.
    """

    # Or mabe get only the 3 most recent
    blogs = Blog.objects.order_by('-date')

    # See that the path is relative to ./templates
    return render(request, 'all_blogs.html', {'blogs': blogs})


def blog_by_id(request, blog_id):
    """
    Render a specific blog identified by its blog id

    Args:
        request (WSGIRequest): This is a subclass of python's
            http.server.BaseHTTPRequestHandler. It represents an incoming http
            request from a client.
        blog_id (integer): Identifier of the blog.

    Returns:
        HttpResponse with arguments containing all the info to render the web
            page.
    """

    blog = get_object_or_404(Blog, pk=blog_id)

    # See that the path is relative to ./templates
    return render(request, 'oneblog.html', {'blog': blog})
