from django import forms
from .models import *

class TicketAddForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ('summary','description')

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs.update({
                "class":"border rounded p-2 w-full bg-gray-200 text-black border-2 border-teal-300",
                "placeholder":f"enter the {field_name}".replace("_","").capitalize()
            })


class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['summary','status','assignee']

    def __init__(self,*args, **kwargs):
            super().__init__(*args,**kwargs)
            for field_name,field in self.fields.items():
                if field_name == 'employee' or field_name == "date" or field_name == "priority" or field_name == "description":
                    field.widget.attrs.update({
                        "class":"border rounded p-2 w-full bg-gray-200 text-black border-2 border-teal-300",
                        "placeholder":f"enter the {field_name}".replace("_","").capitalize(),
                        "disabled":True
                    })
                else:    
                    field.widget.attrs.update({
                        "class":"border rounded p-2 w-full bg-gray-200 text-black border-2 border-teal-300",
                        "placeholder":f"enter the {field_name}".replace("_","").capitalize()
                    })



