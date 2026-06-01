from django.http import HttpResponse

def home(request):
    return HttpResponse('<hr><h2> Internal Employee Ticketing System</h2><hr><h3>version:0.1</h3>')