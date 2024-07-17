
from django import forms
from admin_pannel.models import Mail,contacts



class add_mail(forms.ModelForm):
    address=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control bg-transparent rounded-0 my-4','placeholder':"Your Email Address",'required':'True'}))
   
    class Meta:
        model=Mail
        fields=('__all__')




class contact_form(forms.ModelForm):
    option = {
    "Business Proposal": "Business Proposal",
    "Personal Proposal": "Personal Proposal",
    "Want to Say Hello": "Want to Say Hello",
    }
    first_name=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0'}))
    last_name=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0'}))
    email=forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0'}))
    purpose=forms.ChoiceField(required=True, choices=option, widget=forms.Select(attrs={'class':'form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0'}))
    description=forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0'}))
    class Meta:
        model=contacts
        fields=('__all__')

