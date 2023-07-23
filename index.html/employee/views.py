from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib  import auth
from .forms import EmpForm
from .models import Employee

# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')

def userhome(request):
    return render(request,'userhome.html')

def signuppage(request):
    if request.method =="POST":
       
        username=request.POST['Username']
       
        password=request.POST['password']
    try:
        user=User.objects.get(username=username)
        return render(request,'signup.html')
    except:
        user=User.objects.create_user (username=username,password=password)
        user.save()
        return render(request,'signin.html')
    else:
        return render(request,'signup.html')

def signinpage(request):
    if request.method =="POST":
        username=request.POST['Username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'userhome.html')
        else:
            return render(request,'signup.html')
    else:
        return render(request,'signin.html') 
    
def signout(request):
    auth.logout(request)
    return render(request,'signin.html')

def addemp(request):
     empform=EmpForm
     return render(request,'addemp.html',{'empform':empform})
def insertEmp(request):
    if request.method == "POST":
        empForm = EmpForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            
            return render(request,'get.html')
        else:
            return render(request,'addemp.html')
    else:
        return render(request,'addemp.html')

def getEmp(request):
    employees = Employee.objects.all()
    return render(request,'get.html',{'employees':employees})

def editEmp(request,eid):
    emp = Employee.objects.get(eid=eid)
    return render(request,'edit.html',{'emp':emp})

def updateEmp(request,eid):
    if request.method == "POST":
        emp = Employee.objects.get(eid=eid)
        form = EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return render(request,'get.html')
        else:
            return render(request,'edit.html',{'emp':emp})
    else:
            return render(request,'edit.html', {'emp': emp})

def deleteEmp(request,eid):
    emp = Employee.objects.get(eid=eid)
    emp.delete()
    return render(request,'get.html')

