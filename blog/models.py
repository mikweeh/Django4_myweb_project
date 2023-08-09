# -*- coding: utf-8 -*-

"""
Blog models file.

Remember that when you change your model attributes you need to make migrations
(python3 manage.py makemigrations) and migrate (python3 manage.py migrate)
"""

#############
# Libraries #
#############

from django.db import models
from django.utils import timezone


##################
# Custom classes #
##################

class Blog(models.Model):
    """
    Class Blog. This is the main class of the blog app.

    Args:
        title: Title of the blog
        date: Date when the blog was created
        description: Description of the blog

    Returns:
        Object of the current class
    """

    # Here I describe the fields
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title