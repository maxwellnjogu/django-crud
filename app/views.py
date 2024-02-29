
from django.shortcuts import render,redirect
from .models import Student

# Create your views here.

def index(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)



def insertData(request): 
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        if len(request.FILES) !=0:
            image = request.FILES['image']
        
        query=Student(name=name,email=email,age=age,gender=gender, image=image)
        query.save()
        return redirect("/")

    return render(request,"index.html")



def updateData(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        if len(request.FILES) != 0:
            if len(edit.image) > 0:
                edit.image = request.FILES['image']
        edit.save()
        return redirect("/")

    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    
    return render(request,"index.html")





    

    