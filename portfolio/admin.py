# -*- coding: utf-8 -*-

"""
Admin control of the app portfolio

Remember that each admin.py file inside an application folder must import
the classes from the models.py file in the same folder.
"""

#############
# Libraries #
#############

# Import admin
from django.contrib import admin

# Also import my custom class defined in ./models.py
from .models import Project


##########
# Set up #
##########

# Add the imported classes to admin control
admin.site.register(Project)
