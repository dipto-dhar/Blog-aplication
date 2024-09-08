from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Category,Settings,Mail,contacts,about_content
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class add_admin(UserCreationForm):
    f_name= forms.CharField(
        max_length=40, 
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    l_name= forms.CharField(
        max_length=40,
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    email= forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
   
    username= forms.CharField(max_length=50,label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))




class Meta:
    model=User
    field=('f_name','username','l_name','email','password1','password2')
        








class update_admin(forms.ModelForm):
    
        first_name= forms.CharField(
        max_length=40, 
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        last_name= forms.CharField(
        max_length=40,
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        email= forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
   
        username= forms.CharField(max_length=50,label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

        class Meta:
            model=User
            fields = ('username','email','first_name','last_name')
        







class create_post(forms.ModelForm):
    desc = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model=Post
        fields=('title','desc','image','category','featured')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','required':'False'}),
            
            # 'image': forms.ImageField(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control','required':'False'}),

        }
class create_category(forms.ModelForm):
   
    class Meta:
        model=Category
        fields=('__all__')
        widgets={
            'cat_name': forms.TextInput(attrs={'class':'form-control','required':'True'}),
            
    
        }
class add_mail(forms.ModelForm):
    address=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Recipient's Email",'required':'True'}))
   
    class Meta:
        model=Mail
        fields=('__all__')
        


class modify_settings(forms.ModelForm):
    footer_text=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    fb_link=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    insta_link=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    pinterest_link=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    twiter_link=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    linkedin_link=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    site_name=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    site_title=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
   
    class Meta:
        model=Settings
        fields=('__all__')

class contact_form(forms.ModelForm):
    first_name=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    purpose=forms.ChoiceField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    desc=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=contacts
        fields=('__all__')

class about_form(forms.ModelForm):
    title=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=about_content
        fields=('__all__')