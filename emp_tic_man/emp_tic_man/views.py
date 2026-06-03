from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # return HttpResponse('<hr><h2> Internal Employee Ticketing System</h2><hr><h3>version:0.1</h3>')
    return render(request,'base.html')