from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

def HomeView(request):
    return render(request,'App/base.html')

def IndexView(request):
    context = {'message':'This is Home Page'}
    return render(request, 'App/index.html',context)

@login_required(login_url='login')
def PostView(request):
    post = Post.objects.all()
    return render(request, 'App/index.html',{'post': post})

def GetPostById(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(
            post = post,
            author = request.user,
            comment = comment
        )
    return render(request, 'App/post_details.html',{'post': post})


@login_required(login_url='login')
def DeletePost(request,pk):
    msg = '<h1>Post deleted successfully</h1>'
    post= Post.objects.get(id=pk)
    if request.user == post.author:
        post.delete()
    else:
        return HttpResponse('<h1 style="color:red;">403 Forbidden:</h1><hr><h2>You Can Not Access This Page Because This Post is not created By You ,retry After Some times</h2> ')   
    return redirect('display')


@login_required(login_url='login')
def CreatePost(request):
    if request.method == 'POST':
        Item = Post()
        Item.title=request.POST.get('title')
        Item.Location=request.POST.get('Location')
        Item.description=request.POST.get('description')
        Item.author=request.user
        if len(request.FILES) != 0:
            Item.images = request.FILES['images']
        Item.save()
        return redirect('display')
    return render(request, 'App/post_create.html')


@login_required(login_url='login')
def UpdatePost(request,pk):
    post = Post.objects.get(id=pk)
    if request.user == post.author:
        context = {'post':post}
        if request.method == "POST":
            post.title = request.POST.get('title')
            post.Location = request.POST.get('Location')
            post.description = request.POST.get('description')
            post.save()
            return redirect('display')
        return render(request, 'App/post_update.html',context)
    else:
        return HttpResponse('<h1 style="color:red;">403 Forbidden:</h1><hr><h2>You Can Not Access This Page</h2>')   
        
    
@login_required(login_url='login')
def ContactUsPage(request):
    return render(request, 'App/contactus.html')

def SendMail(request):

    if request.method == 'POST':
        
        Name=request.POST.get('Name')
        Phone=request.POST['Phone']
        message=request.POST['msg']
        from_email=settings.EMAIL_HOST_USER 
        send_mail(Name ,Phone, message, from_email, ['rajeshlenka19999@gmail.com'], fail_silently=False)
        
        return HttpResponse('Mail Sent..')
    return render(request,'App/post_create.html')


        
def LoginPage(request):
    return render(request,'App/login.html')

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('display')
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('display')
        else:
            context ={"message" : "incorrect Username or Password"}       
    return render(request,'App/login.html',context)
    
@login_required(login_url='login')
def LogoutView(request):
    logout(request)
    return render(request, 'App/index.html')


def RegisterPage(request):
    return render(request,'App/register.html')

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('display')
    context={}
    if request.method == 'POST':
        
        username = request.POST.get('username')
      
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            user = User.objects.create( username=username, email=email, password=password1)
            user.save()
            
            login(request, user)
            return redirect('display')
        else:
            context ={"message" : "Both Password Does Not match Please Recheck It."}       
    return render(request,'App/register.html',context)


def MyAccountPage(request):
    return render(request,'App/Myaccount.html')

@login_required(login_url='login')
def MyAccountView(request):
    
    user = request.user
    user_posts = Post.objects.filter(author=user)
    context = {"posts" : user_posts}
    context["capitalize_username"] = request.user.username.capitalize()
    return render(request,'App/Myaccount.html',context)