from django.shortcuts import render,redirect

# Create your views here.
from .models import Member
def index(request):
    mem=Member.objects.all()
    return render(request,"index.html",{'mem':mem})

def add(request):
    return render(request,"add.html")

def addrec(request):
    x=request.POST['first']
    y=request.POST['first']
    z=request.POST['first']
    mem=Member(first_name=x,last_name=y,address=z)
    mem.save()
    return redirect("/")
def delet(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")