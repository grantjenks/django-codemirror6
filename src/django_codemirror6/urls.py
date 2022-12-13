from django.urls import path

import django_codemirror6.views

urlpatterns = [
    path('', django_codemirror6.views.demo, name='demo'),
]
