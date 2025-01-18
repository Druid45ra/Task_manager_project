from django.http import HttpResponse

def index(request):
    return HttpResponse("Bine ai venit în aplicația Tasks!")
