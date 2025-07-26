from django.shortcuts import render

# Create your views here.
def home(request):
    age=34
    name="Rohit"
    marks=89
    courses=["Python","java","C","Testing"]
    status=True
    context={"data":age,"Data1":name,"data2":marks,"data3":courses,"status":status}
    return render(request,'home.html',context)