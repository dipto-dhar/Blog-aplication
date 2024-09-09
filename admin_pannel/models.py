from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from django_currentuser.db.models import CurrentUserField
from autoslug import AutoSlugField


class Category(models.Model):
    cat_name=models.CharField(max_length=200)
    cat_image=models.ImageField(max_length=250,null=True,blank=True,default=True)
    slug=AutoSlugField(populate_from='cat_name',default=None,null=True,unique=True)
    def __str__(self):
        return self.cat_name
class Mail(models.Model):
    address=models.EmailField()

    def __str__(self):
        return self.e_mail

class Post(models.Model):
    title= models.CharField(max_length=200,blank=True, null=True)
    desc=RichTextUploadingField(blank=True, null=True)
    image=models.ImageField(upload_to='blog_images/',null=True,blank=True)
    date=models.DateField(auto_now_add=True,blank=True, null=True)
    # update_date=models.DateField(auto_now=True,blank=True, null=True, default='')
    category=models.ForeignKey(Category, null=True,related_name='posts', on_delete=models.SET_NULL,default=True)
    author= CurrentUserField()
    # comment=models.TextField(max_length=500)
    featured=models.BooleanField()
    slug=AutoSlugField(populate_from='title',default=None,null=True,unique=True)



    def __str__(self):
        return self.title
    
class Settings(models.Model):
    site_name=models.CharField(max_length=80)
    site_title=models.CharField(max_length=80)  
    logo=models.ImageField(upload_to='site_images/', default=True)
    fav_icon=models.ImageField(upload_to='site_images/')
    fb_link=models.CharField(max_length=240)
    insta_link=models.CharField(max_length=240)
    twiter_link=models.CharField(max_length=240)
    linkedin_link=models.CharField(max_length=240)
    pinterest_link=models.CharField(max_length=240)
    footer_text=models.CharField(max_length=240,default='',null=True)
 


   
    def __str__(self):
        return self.site_name
    



class about_content(models.Model):
    title= models.CharField(max_length=200,blank=True, null=True)
    desc=RichTextUploadingField(blank=True, null=True)
    def __str__(self):
        return self.title

class contacts(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
   
    email= models.EmailField(max_length=50)

    purpose=models.CharField( max_length=50)
    description=models.CharField(max_length=1500)
    def __str__(self):
        return self.first_name