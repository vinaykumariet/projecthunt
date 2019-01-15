from django import forms
from .models import Student
from django.utils import timezone
class student_form(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    email_id=forms.CharField(widget=forms.EmailInput(),required=True,max_length=100)
    contact_no=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    city=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    #dat=timezone.datetime.now()
    

    class Meta():
        model=Student
        fields=['name','email_id','contact_no','city']

