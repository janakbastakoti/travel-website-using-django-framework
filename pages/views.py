from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Destination, Experience, Blog
from .form import CreateBlog, RawCreate

# Create your views here. CreateBlog,






def index_page(request):
    dest       = Destination.objects.all()
    expe       = Experience.objects.all()
   
    return render(request,'index.html', {'dest':dest,'expe':expe })

def contact_page(request):
    return render(request,'contact.html',{})

def blog_page(request):
    blog = Blog.objects.all()
    return render(request,'blog.html',{'blog': blog})






# to save the data in database 
# def addblog_page(request):
#     form = CreateBlog(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = CreateBlog(request.POST or None)
#     return render(request,'add_blog.html',{'form':form})
# change the saved data from the database
def addblog_page(request):
    obj = Blog.objects.get(id=10)
    form = CreateBlog(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form = CreateBlog(request.POST or None)
    return render(request,'add_blog.html',{'form':form})



# def addblog_page(request):
#     form = RawCreate()
#     if request.method == 'POST':
#         form = RawCreate(request.POST)
#         if form.is_valid():
#             print('ok')
#             print(form.cleaned_data)
#             Blog.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#         return render(request,'add_blog.html',{'form':form})
#     else:
#         return render(request,'add_blog.html',{'form':form})
    

def about_page(request):
    return render(request,'about.html',{})

def settings_page(request):
    return render(request,'settings.html',{})

def logout_page(request):
    auth.logout(request)
    return redirect('/')



def login_page(request):
    if request.method == 'POST':
        user_name    = request.POST['username']
        password    = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request,user)
            print(user)
            return render(request,'account.html',{})
        else:
            messages.info(request,'doesnot have account')
            return redirect('login')
    else:
        return render(request,'login.html',{})



def register_page(request):
    # print(request.method)
    print('ok')
    if request.method == "POST":
        print('ok')
        first_name   = request.POST['fname']
        last_name    = request.POST['lname']
        user_name    = request.POST['username']
        email        = request.POST['email']
        password1    = request.POST['password1']
        password2    = request.POST['password2']
        print("input taken")
        print(first_name)
        print(last_name)
        print(user_name)
        print(password1)
        print(password2)
        print(email)
        if password1 == password2:  
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email= email).exists():
                messages.info(request,'account exits with email')
                return redirect('register')
            else:                                  
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save();
                print('user created')        
                print(request.method)  
                return redirect('login')
        else:
            messages.info(request,'password doesnot match')
            return redirect('register')
       
    else:
        return render(request,'register.html',{})

def account_page(request):
    return render(request,'account.html',{})
    
    
    

