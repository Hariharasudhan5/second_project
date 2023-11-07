from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def silk(request):
    return HttpResponse('<h1><marquee>we are not talking about Dairymilk silk</h1></marquee> ')

