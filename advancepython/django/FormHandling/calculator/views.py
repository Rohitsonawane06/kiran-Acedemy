from django.shortcuts import render

# Create your views here.
def calculate(request):
    if request.method=="POST":
        a=int(request.POST.get("fno"))
        b=int(request.POST.get("fno"))
        opr=request.POST.get("opr")
        if(opr=="+"):
            c=a+b
        elif(opr=="-"):
            c=a-b
        elif(opr=="*"):
            c=a*b
        else:
            c=a/b
        return render(request,'calculator/cal.html',{'result':c,'a':a,'b':b})
    else:

        return render(request,'calculator/cal.html',)