from django.shortcuts import render , HttpResponse , redirect
from datetime import datetime
from icecream.models import Contact , Signup
from django.contrib import messages , auth
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'base1.html')

def home(request):
    return render(request, 'base1.html')
    
def contact(request):   
     if request.method== "POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          order=request.POST.get('order')
          time=request.POST.get('time')
          ice=request.POST.get('ice')
          instruct=request.POST.get('instruct')
          contact = Contact(name=name , email=email , phone=phone , order=order , time=time , ice=ice , instruct=instruct , date= datetime.today())
          contact.save()


     return render(request, 'base1.html')
    
def login(request):


    if request.method == 'POST':
        # login user
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            #return render(request, 'base1.html', {'success': 'You are successfully logged in!'})
            return redirect('homepage')
        else:
            return render(request, 'logsign.html', {'error': True})
    else:
        # user wants to login
        return render(request, 'logsign.html')

        

def signup(request):

    if request.method == 'POST':
        
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        signup = Signup(username=username , fname=fname )
        signup.save()
    
    
    if request.method == 'POST':
        # sign up the user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'logsign.html', {'error1': True})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                #return render(request, 'base1.html', {'success1': 'You are successfully registered and logged in!'})
                return redirect('homes')
        else:
            return render(request, 'logsign.html', {'error2': True })
    else:
        # user wants to sign up
        return render(request, 'logsign.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('homepage')