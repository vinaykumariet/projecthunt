from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Product(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    votes=models.IntegerField(default=1)
    body=models.TextField()
    url=models.TextField()
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)


    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title    

class Student(models.Model):
    name=models.CharField(max_length=255)
    email_id=models.EmailField(max_length=50)
    contact_no=models.CharField(max_length=11)
    dat=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.email_id       

