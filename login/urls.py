from django.urls import path
from login import views
from .views import *

urlpatterns = [
    path('', views.index),
    # path('' ,hello_world, name='home') //uncomment this ans comment the ablve path to generate Error 500

]