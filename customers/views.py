from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . models import Customer
def sign_out(request):
    logout(request)
    return redirect('home')
    
# Create your views here.
def show_account(request):
    if request.POST and 'register' in request.POST:
        try:    
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #create user accounts 
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            # create customer account
            customer=Customer.objects.create(
                name = username,
                user=user,
                phone=phone,
                address=address
            )
            return redirect('home')
        except Exception as e: 
            error_message="Duplicate username or invalid credentials"
            messages.error(request,error_message)  
    if request.POST and 'login' in request.POST:
        username=request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(username=username,password=password)
        print('user while login\n',user)
        if user:
            login(request,user)
            print('login successsfull')
            
    
            return redirect('home')
        else:
            messages.error(request,"Invalid User Credentials")
    return render(request,'account.html')