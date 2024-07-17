from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import add_admin
from django.contrib.auth.models import User
from django.db import models
from .models import Category,Post,Settings,Mail,contacts,about_content
from .forms import create_post,create_category,modify_settings,add_mail,update_admin,about_form
from django.db.models import Count


site_data=Settings.objects.get(id=1)
    

def admin_login(request):
    
    if request.user.is_authenticated:    
        return render(request,'admins/dashboard.html',{'site':site_data})
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']

            user= authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Succcessfully logged in")
                return redirect('dashboard')
        else:
            return render(request,'admins/index.html',{'site':site_data})

def admin_logout(request):
    logout(request)
    return redirect('admin_pannel')


def admin_register(request):
    form=add_admin()
    if request.method=='POST':
        form=add_admin(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Successfully Created")
            return render(request,'admins/add-user.html',{'form':form,'site':site_data})         
    else:
        form=add_admin()
        
    return render(request,'admins/add-user.html',{'form':form,'site':site_data})

def profile(request):
   
  
    form=update_admin(request.POST, instance=request.user)
    if request.method=='POST':
         form=update_admin(request.POST, instance=request.user)
         if form.is_valid():
             form.save()
             messages.success(request,"Your Profile Has Been Successfully Updated")
                   
    else:
         form=update_admin(instance=request.user)

        
    return render(request,'admins/user-profile.html',{'form':form,'site':site_data})

    # post=Post.objects.get(id=pk)
    # form = create_post(instance = post)
    # if request.method == 'POST':
    #     form = create_post(request.POST, request.FILES, instance=post)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"The Post Has Been Updated Successfully")
    #         return redirect('posts')

    # return render(request,'admins/edit-post.html',{'form':form,'site':site_data})

# def add_post(request):
#     cat=Category.objects.all()
#     if request.method=='POST':
#          title= request.POST.get('postTitle')
#          desc= request.POST.get('postContent')
#          image= request.FILES.get('postImage')
#          category= request.POST.get('postCategory')
#          category_obj = Category.objects.get(id=category)

#          data=Post(title=title,desc=desc,image=image,category=category_obj)
#          data.save()
#          return render(request,'admins/posts.html',{})
  
#     return render(request,'admins/add-post.html',{'cat':cat})
    # form=add_post()
    # return render(request,'admins/add-post.html',{'form':form})

def add_post(request):
    form=create_post()
    
    if request.method=='POST':
        form=create_post(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"The Post Has Been Created Successfully")
            return redirect("posts")
    
    return render(request,'admins/add-post.html',{'form':form,'site':site_data})


def show_posts(request):
    posts=Post.objects.order_by('-date')
    
    return render(request,'admins/posts.html',{'posts':posts,'site':site_data})

def delete_posts(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    messages.success(request,"The Post Has Been Deleted Successfully")
    return redirect('posts')
def edit_posts(request,pk):


    post=Post.objects.get(id=pk)
    form = create_post(instance = post)
    if request.method == 'POST':
        form = create_post(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,"The Post Has Been Updated Successfully")
            return redirect('posts')

    return render(request,'admins/edit-post.html',{'form':form,'site':site_data})







def add_category(request):
    form=create_category()
    
    if request.method=='POST':
        form=create_category(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"The Post Has Been Created Successfully")
            return redirect("categories")
    
    return render(request,'admins/add-category.html',{'form':form,'site':site_data})

def show_categories(request):
    # categories=Category.objects.all()
    categories = Category.objects.annotate(numposts = Count("posts")).all()
    return render(request,'admins/category.html',{'categories':categories,'site':site_data})




def delete_category(request,pk):
    category=Category.objects.get(id=pk)
    category.delete()
    messages.success(request,"The Category Has Been Deleted Successfully")
    return redirect('categories')

def edit_category(request,pk):
    category=Category.objects.get(id=pk)
    form = create_category(instance = category)
    if request.method == 'POST':
        form = create_category(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request,"The Category Has Been Updated Successfully")
            return redirect('categories')

    return render(request,'admins/edit-category.html',{'form':form,'site':site_data})




def settings(request):


    settings_data=Settings.objects.get(id=1)
    form = modify_settings(instance = settings_data)
    if request.method == 'POST':
        form = modify_settings(request.POST, request.FILES, instance=settings_data)
        if form.is_valid():
            form.save()
            messages.success(request,"The Settings Has Been Saved Successfully")
            return redirect('settings')

    return render(request,'admins/settings.html',{'form':form,'site':site_data})



def mails(request):
    form=add_mail()
    
    if request.method=='POST':
        form=add_mail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"The Mail Has Been Added Successfully")
            return redirect("mails")
    else:
        mails = Mail.objects.all()
        return render(request,'admins/mail.html',{'form':form,'mails':mails,'site':site_data})
    

def delete_mail(request,pk):
    mail=Mail.objects.get(id=pk)
    mail.delete()
    messages.success(request,"The Mail Has Been Removed Successfully")
    return redirect('mails')

def contact(request):
    # categories=Category.objects.all()
    contact = contacts.objects.all()
    return render(request,'admins/contacts.html',{'contacts':contact,'site':site_data})

def delete_contact(request,pk):
    contact=contacts.objects.get(id=pk)
    contact.delete()
    messages.success(request,"The Record Has Been Removed Successfully")
    return redirect('contacts')



def about(request):
    page_data=about_content.objects.get(id=1)
    form=about_form(instance=page_data)
    if request.method=='POST':
        form=about_form(request.POST,instance=page_data)
        if form.is_valid():
            form.save()
            messages.success(request,"The Page Has Been Updated Successfully")
            return redirect("about")
    else:
        mails = Mail.objects.all()
        return render(request,'admins/about.html',{'form':form,'site':site_data})