from django.http import HttpResponse


def home_view(request):
    return HttpResponse("<h2 style='text-align: center'>Hello World!</h2>")
