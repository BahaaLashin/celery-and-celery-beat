from django.urls import path 
from .views import *

urlpatterns = [
 
    path('',get_dommy_data,name='domydata')
]
