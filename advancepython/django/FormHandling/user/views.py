from django.shortcuts import render

# Create your views here.
def adduser(request):
    if request .method=="post":
        print("post method")
        uid=request.POST.get("uid")
        uname=request.POST.get("uname")
        em=request.POST.get("email")
        password=request.POST.get("password")
        context={"uid":uid,"Uname":uname,"em":em,"password":password}
        return render(request,'user/adduser.html',context)
    else:
        print("Get method")
        return render(request,'user/adduser.html')