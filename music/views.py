from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Heading1</h1>")


def special_case_2018(request):
    return HttpResponse("Testing")


def get_year(request, year):
    return HttpResponse("<h1> The Year value is: "+str(year)+"</h1>")

