from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm 

# Create your views here.

def index(request):
  form = CustomerForm()
  if request.method == 'POST':
    print(request.POST)
    form = CustomerForm(request.POST)
    if form.is_valid():
      form.save()
  context = {"form":form}
  return render(request, 'index.html', context)