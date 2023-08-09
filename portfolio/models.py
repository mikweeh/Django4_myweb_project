# -*- coding: utf-8 -*-

"""
Portfolio models file

Remember that when you change your model attributes you need to make migrations
(python3 manage.py makemigrations) and migrate (python3 manage.py migrate)
"""

#############
# Libraries #
#############

from django.db import models


##################
# Custom classes #
##################

class Project(models.Model):
    """
    Class Project. This is the main class of the portfolio app.

    Args:
        title: Title of the project
        description: Description of the project
        image: Image of the project
        url (optional): Url to the project

    Returns:
        Object of the current class
    """

    # Description of the fields
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    # Fíjate que al cargar la imagen pones una ruta relativa. Esta ruta es
    # relativa respecto a 'MEDIA_ROOT' si está definida en settings, o bien
    # respecto a BASE_DIR en caso contrario. En esta ruta se guarda la imagen.
    image = models.ImageField(upload_to='portfolio/images/')

    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
