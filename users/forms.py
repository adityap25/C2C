from cProfile import label
from django import forms
from .models import CompanyProfile, TpoProfile, User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    type_choices=(("TPO","TPO"),("Company","Company"))
    type=forms.ChoiceField(choices=type_choices,label="Type of Organization",required=True)
    name=forms.CharField(max_length=50,required=True)
    phone=forms.CharField(max_length=12)
    class Meta:
        model=User
        fields=('email','name','phone','type','password1','password2')
        # def __init__(self,*args,**kwargs):
        #     super().__init__(*args,**kwargs)
        #     for field in self.fields:
        #         self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('email','name','phone')

class UpdateTpoProfileForm(forms.ModelForm):
    status_choices=(("HIRING","HIRING"),("NOT HIRING","NOT HIRING"))
    status=forms.ChoiceField(choices=status_choices,label="STATUS",required=True)
    class Meta:
        model =TpoProfile
        fields=('status','min_ctc','image','desc')

class UpdateCompanyProfileForm(forms.ModelForm):

    class Meta:
        model =CompanyProfile
        fields=('location','sector','image','desc')