from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email



class Userform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),required=True,max_length=50)
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}),required=True,max_length=50)
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),required=True,max_length=50)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}),required=True,max_length=50)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}),required=True,max_length=50)
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter confirm password'}),required=True,max_length=50)

    class Meta():
        model=User
        fields=['username','email','first_name','last_name','password']

    def clean_username(self):
        user=self.cleaned_data['username']
        try:
            match=User.objects.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError(" Username already exists")
    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            m1=validate_email(email)
        except:
            return email 
        raise forms.ValidationError(" Email is not correct format")
        
    def clean_confirm_password(self):
        pas=self.cleaned_data['password']
        cpas=self.cleaned_data['confirm_password']
        MIN_LENGHT=8
        if pas and cpas:
            if pas != cpas:
                raise forms.ValidationError('not match')
            else:
                if len(pas)<MIN_LENGHT:
                    raise forms.ValidationError('should be 8')
                if pas.isdigit():
                        raise forms.ValidationError('password  not numbric')












