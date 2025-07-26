from django.shortcuts import render

# Create your views here.
def marksheet(request):
    if request.method == "POST":
        sname = request.POST.get("sname")
        m1 = int(request.POST.get("m1"))
        m2 = int(request.POST.get("m2"))
        m3 = int(request.POST.get("m3"))

        total = m1 + m2 + m3
        percentage = total / 3

        if percentage >= 75:
            grade = 'A'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C'
        elif percentage >= 40:
            grade = 'D'
        else:
            grade = 'F'
        
        return render(request,'marksheet/marksheet.html',
                      {
                          'sname':sname,
                          'm1':m1,
                          'm2': m2,
                          'm3' : m3,
                          'total': total,
                          'percentage' : percentage,
                          'grade' : grade
                      })
    else:
        return render(request,'marksheet/marksheet.html')