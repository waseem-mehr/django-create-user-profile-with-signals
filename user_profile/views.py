from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
# Create your views here.

def home(request):
  
  return render(request,'user_profile/index.html')

@login_required(login_url='/')
def profile(request):
  p=Profile.objects.get(user=request.user)
  context={
    'profile':p
  }  
  return render(request,'user_profile/profile.html',context)


def log_in(request):
  if request.method=='GET':
    return render(request,'user_profile/login.html')
  elif request.method=='POST':
    user=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
    print(user)
    if user is not None:
      login(request,user)
      return redirect('/')
    else:
      return redirect('/login')

def signup(request):
  if request.user.is_authenticated:
      return redirect('/')
  else:
    if request.method=='GET':
      context={
        'form':UserCreationForm()
      }
      return render(request,'user_profile/signup.html',context)
    elif request.method=='POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('/login')
      else:
        return redirect('/signup')

@login_required(login_url='/login')
def log_out(request):
  logout(request)
  return redirect('/')

@login_required(login_url='/login')
def edit(request):
  user=Profile.objects.get(user=request.user)
  if request.method=='GET':
    form=ProfileForm(instance=user)
    context={
      'form':form,
    }
    return render(request,'user_profile/edit.html',context)
  if request.method=='POST':
    form=ProfileForm(request.POST,request.FILES,instance=user)
    if form.is_valid():
      form.save()
      return redirect('/profile')
    else:
      return HttpResponse('not changed the profile')  