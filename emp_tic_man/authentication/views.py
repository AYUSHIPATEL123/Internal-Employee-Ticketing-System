from django.shortcuts import render,redirect
from django.views import View
from .forms import UserForm
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

        