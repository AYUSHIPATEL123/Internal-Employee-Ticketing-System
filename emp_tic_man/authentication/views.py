from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import View
from .forms import *
# Create your views here.


class RegisterView(View):
    form_class=UserForm
    template_name="auth/register.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
        
        return render(request, self.template_name, {"form": form})    

def login_(request):
    form = Loginform()
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request,email=email,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None,"invalid cradentials...!")
                return render(request,'auth/login.html',{"form":form})
        
    return render(request,'auth/login.html',{"form":form}) 

   