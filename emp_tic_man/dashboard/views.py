from django.shortcuts import render

# Create your views here.


def staff(request):
    return render(request,'dashboard/it_stf_dashboard.html')


def manager(request):
    return render(request,'dashboard/man_dashboard.html')