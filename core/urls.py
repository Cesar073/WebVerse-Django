from django.urls import path

import core.views as views

urlpatterns = [
    path('', views.index),
]