from django.shortcuts import render
from .models import profile
from django.shortcuts import render , HttpResponseRedirect ,redirect,HttpResponse
from django.contrib.auth.models import User , auth
from django.db.models import Exists 
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password1']
        password1=request.POST['password2']

        if password == password1:
            if profile.objects.filter(email=email).exists():
                print("email already used")
                       
            else:
                var=profile(email=email,password=password)
                print("user created")
                var.save()     
                return render(request,"login.html")           
        else:
            print("password doesnt match")          
            return redirect("register")

    obj1=profile.objects.all()
    return render(request,"register.html",{'data1':obj1})


def login(request):
    if request.method == 'POST':
        email1=request.POST['email']
        password=request.POST['password']

        var=profile.objects.filter(email=email1)

        for i in var:
            pass1=i.password
            em=i.email

        if em==email1:
            if password==pass1:
                request.session['name']=email1
                return redirect("index")
                print("logged in")
            else:
                print("password does not match")
                return redirect('/')
        else:
            print("email does not exist")
            return redirect('/')
    else:
        return render(request,"login.html")

def index(request):
    return render(request,'index.html')