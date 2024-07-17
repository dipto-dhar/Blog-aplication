from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import models
from admin_pannel.models import Category,Post,Settings,contacts,about_content
from .forms import add_mail,contact_form
from django.contrib import messages



site_data=Settings.objects.get(id=1)


def index(request):
    posts=Post.objects.order_by('-date')
    title=site_data.site_name +" - " + site_data.site_title
    featured_posts=Post.objects.filter(featured=True)
    mail_form=add_mail()
    if request.method=='GET':
        query=request.GET.get('Search')
        if query != None:
            posts=Post.objects.filter(title__icontains=query)
    if request.method=='POST':
        mail_form=add_mail(request.POST)
        if mail_form.is_valid():
            mail_form.save()
            messages.success(request,"Subscribe Successfully")
            return redirect("home")
        
    return render(request,'frontend/index.html',{'posts':posts,'title':title,'site_data':site_data,'featured_posts':featured_posts,'mail_form':mail_form})

def about(request):
    title="About"+ " - " + site_data.site_name
    content=about_content.objects.get(id=1)
    title=content.title + " - " + site_data.site_name
    
    return render(request,'frontend/about.html',{'title':title,'content':content, 'site_data':site_data})
    
def contact(request):
    title="Contact"+ " - " + site_data.site_name
    form=contact_form()
    if request.method=='POST':
        form=contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Submited Successfully")
            return redirect("contact")
    return render(request,'frontend/contact.html',{'title':title,'form':form, 'site_data':site_data})

def show_single_post(request,slug):
    post=Post.objects.get(slug=slug)
    title=post.title + " - " + site_data.site_name
    return render(request,'frontend/single-post.html',{'post':post, 'title':title,'site_data':site_data})

    

def category(request):
    # categories=Category.objects.all()
    categories = Category.objects.all()
    return render(request,'frontend/category.html',{'categories':categories,'site_data':site_data})

def single_category(request,slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    title=category.cat_name + " - " + site_data.site_name
    
    posts=Post.objects.filter(category=category)


    return render(request,'frontend/single-category.html',{'posts':posts,'title':title,'site_data':site_data,'categories':categories})


 