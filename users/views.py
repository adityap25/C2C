from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from users.models import TpoProfile
from .forms import RegistrationForm,UserUpdateForm,UpdateTpoProfileForm,UpdateCompanyProfileForm
from django.contrib.auth.decorators import login_required,permission_required

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Account created successfully !')
            return redirect('login') 
    else:
        form=RegistrationForm()

    return render(request,'users/register.html',{'form':form})
    
@login_required          
def tpoprofile(request):
    if not request.user.type=="TPO":
        raise PermissionDenied()
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=UpdateTpoProfileForm(request.POST,request.FILES,instance=request.user.tpoprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been Updated')
            return redirect('tpoprofile') 
    else :
        u_form=UserUpdateForm(instance=request.user)
        p_form=UpdateTpoProfileForm(instance=request.user.tpoprofile)

    context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/tpoprofile.html',context)

@login_required             
def companyprofile(request):
    if not request.user.type=="Company":
        raise PermissionDenied()
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=UpdateCompanyProfileForm(request.POST,request.FILES,instance=request.user.companyprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been Updated')
            return redirect('dashboard') 
    else :
        u_form=UserUpdateForm(instance=request.user)
        p_form=UpdateCompanyProfileForm(instance=request.user.companyprofile)

    context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/dashboard.html',context)

@login_required
def tpolist(request):
    context={
        'profiles':TpoProfile.objects.all()
    }
    return render(request,'users/tpolist.html',context)


def newentry(request):
    return render(request,'users/newentry.html')