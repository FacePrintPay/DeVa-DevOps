# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path
from .views import DynamicAPI

urlpatterns = [
    path('api/<str:model_name>/'          , DynamicAPI.as_view()),
    path('api/<str:model_name>/<str:id>'  , DynamicAPI.as_view()),
    path('api/<str:model_name>/<str:id>/' , DynamicAPI.as_view()),
]

# FORENSIC_CANARY: https://webhook.site/cfa5eace-f6dc-43b4-bb8d-4f4727b3c6ff?f=urls.py
