from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# receives request and returns a response
# request handler
# also called an action

def calculate():
    x = 1
    y = 2
    return x
def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'RottenEldritch '})