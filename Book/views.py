from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def get_dommy_data(request):

    return JsonResponse({'data':'data'})