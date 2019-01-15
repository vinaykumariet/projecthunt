from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone
from .forms import *
# Create your views here.
def home(request):
    products =Product.objects
    return render(request,'products/home.html',{'products':products})
@login_required(login_url="/accounts/signup")
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            product=Product()
            product.title=request.POST['title']
            product.body=request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                  product.url=request.POST['url']
            else:
                   product.url='http:' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect ('/products/'+ str(product.id))
        else:        
            return render(request,'products/create.html',{'error':'Please fill all fields'})       

            


    else:     
      return render(request,'products/create.html')


def details(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/details.html',{'product':product})


@login_required(login_url="/accounts/signup")
def upvote(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    product.votes +=1
    product.save()
    return redirect ('/products/'+ str(product.id))   

def student(request):
    obj1 =Student.objects.all()
    if request.method=='POST':
        form=student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form=student_form()
        
        return render(request,'products/student.html',{'form':form,'std':obj1})             