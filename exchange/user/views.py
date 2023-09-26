from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Userupdateform

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:home')
        else:
            messages.error(request, "invalid user")
    return render(request,'login.html')


def register(request):
    p = None
    if(request.method=="POST"):
        u =request.POST['u']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        try:
            if(User.objects.get(username=u)):
                messages.error(request, "username not available")
        except:
            if(p):
                if(p==cp):
                    u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
                    u.save()
                    return user_login(request)
                else:
                    messages.error(request,"PASSWORDS ARE NOT SAME")
            else:
                messages.error(request, "please enter password")

    return render(request,'register.html')


@login_required
def updateuser(request):
    user=request.user
    form=Userupdateform(instance=user)

    if(request.method == "POST"):
        form =Userupdateform(request.POST,instance=user)
        if form.is_valid():
            form.save()

    return render(request,'update_profile.html',{'form':form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:home')

