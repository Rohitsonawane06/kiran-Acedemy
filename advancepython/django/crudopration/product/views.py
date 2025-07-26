
from django.shortcuts import render,redirect
from .models import product 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def show(request):
    data=product.objects.all()
    print('product data : \n',data[0].productimages)
    context={"info":data}
    return render(request,'show.html',context)
@login_required
def add(request):
   if request.method == "POST":
        pname = request.POST['pname']
        price = request.POST['price']
        offer = request.POST['offer']
        description = request.POST['description']
        category = request.POST['category']
        productimages = request.FILES['productimages']
        obj=product(pname=pname,price=price,offer=offer,productimages=productimages,description=description,category=category)
        obj.save()
        return redirect("show")
   else:   
        return render(request,"add.html")
   
def edit(request,id):
    obj = product.objects.get(id=id)
    if request.method=="POST":
        pname = request.POST['pname']
        price = request.POST['price']
        offer = request.POST['offer']
        description = request.POST['description']
        category = request.POST['category']
        productimages = request.FILES['productimages']
        obj.pname=pname
        obj.price=price
        obj.offer=offer
        obj.description=description
        obj.category=category
        obj.productimages
        obj.save()
        return redirect("show")
    return render(request,'edit.html',{"data":obj})


def delete(request,id):
    obj=product.objects.get(id=id)
    obj.delete()
    return redirect("show")


def search_view(request):
    category = request.GET.get('category')
    query = request.GET.get('query')
    results = product.objects.all()

    if category:
        results = results.filter(category__iexact=category)  # assuming you have a 'category' field
    if query:
        results = results.filter(productname__icontains=query)

    return render(request, 'search_results.html', {'results': results})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
             return render (request,'login.html',{"error" : "User Not Found Please Try Again.."})

        if not check_password(password,user.password):
            return render(request,"login.html",{"error":"Invalid password..please Enter Correct Password"})
        user = authenticate(request, username=username, password=password)
        if user.password  != password:
                 return render(request,"login.html",{"error":"Invalid password..please Enter Correct Password"})
        else:
                login(request, user)
                return redirect('show')
    else:
            return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email=request.POST.get('email')
        password = request.POST.get('password')
        #user = authenticate(request, username=username, password=password)

        if User.objects.filter(username=username).exists():
            return render (request,"register.html",{"error":"user is already register"})
        else:
            User.objects.create_user(username=username,email=email,password=password)
            return redirect('login')
        

    return render(request, 'register.html')


def logoutU(request):
     logout(request)
     return redirect("login")
