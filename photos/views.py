from django.shortcuts import render
from django.http import HttpResponse

#Home view
def index(request):
    return render(request, 'index.html')
