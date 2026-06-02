from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser
class UserForm(forms.ModelForm):

    confirm_password=forms.CharField(max_length=300,required=True,widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm Password"
    }))

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','username','phone','address','role','password','confirm_password']

    def clean(self):
        data = super().clean()
        
        if data['password'] != data['confirm_password']:
            raise ValidationError("password dose not mached")

        if len(data['password']) < 8:
            raise ValidationError("password should contail 8 characters")

        return data
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for field_name,field in self.fields.items():
            field.widget.attrs.update({
                "class":"border rounded p-2 w-full bg-gray-200 text-black",
                "placeholder":f"enter the {field_name}".replace("_","").capitalize()
            })


    def save(self, commit = True):
        
        user = super().save(commit=False)
        user.set_password('password')
        if commit:
            user.save()

        return user

class Loginform(forms.Form):
    email = forms.CharField(max_length=300)
    password= forms.CharField(max_length=200,required=True,widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm Password"
    }))
