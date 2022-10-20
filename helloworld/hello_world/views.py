from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Testing SSL Django Deployment</h1>")


def welcome(request):
    return HttpResponse("<h2>Testing a second endpoint!</h2>")