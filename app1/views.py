from django.shortcuts import render
from django.http import HttpResponse
from .models import Database1

# Create your views here.

def home(request):
    return render(request,'index1.html')

def home2(request):

    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    phone = request.GET.get('phone', '')
    collage = request.GET.get('collage', '')
    year = request.GET.get('year', '')
    course = request.GET.get('course', '')

    database1 = Database1(name=name, email=email, collage=collage, phone=phone, year=year, course=course)
    database1.save()

    #return HttpResponse()
    return render(request,'ok.html')

# pulling all data from database
def home3(request):
    data = Database1.objects.all()

    args = {'data':data}
    return render(request,'show.html',args)

def home4(request):
    return render(request,'examp1.html')

def home5(request):
    names = request.GET.get('name','')
    courses = request.GET.get('course','')
    collages = request.GET.get('collage','')

    if names == "" and collages == "":
        post = Database1.objects.filter(course=courses)
    elif names == "" and courses == "":
        post = Database1.objects.filter(collage=collages)
    elif courses == "" and collages == "":
        post = Database1.objects.filter(name=names)
    elif names == "":
        post = Database1.objects.filter(course=courses , collage=collages)
    elif courses == "":
        post = Database1.objects.filter(name=names , collage=collages)
    elif collages == "":
        post = Database1.objects.filter(name=names , course=courses)
    else:
        post = Database1.objects.filter(course=courses , name=names , collage=collages)

    args={'data':post}
    if names == "" and collages == "" and courses == "":
        return HttpResponse(" <h1> Please fill information to see details </h1>")
    else:
        return render(request,'result.html',args)
