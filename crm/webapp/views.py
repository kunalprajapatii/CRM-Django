from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms  import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import customer
from django.contrib import messages

# Create your views here.

# Home page
def home(request):
    # return HttpResponse("hello g kese ho ")
    
    return render(request, 'webapp/index.html')

# Register  user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Create Successfully")
            return redirect('my-login')
    
    context = {'form':form}
    return render(request,'webapp/register.html',context=context)


#login page

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request," Logged-in ")
                return redirect('dashboard')
    context = {'form':form}
    return render(request,"webapp/my-login.html",context = context)


# dashboard 

@login_required(login_url='my-login')
def dashboard(request):
    my_records = customer.objects.all()
    context={'records':my_records}
    return render(request, 'webapp/dashboard.html', context=context)

#create record
@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    if request.method =='POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Created Successfully")
            return redirect('dashboard')
    context ={'form':form}    
    return render(request,'webapp/create-record.html', context=context)


#update record
@login_required(login_url='my-login')
def update_record(request, pk):
    record = customer.objects.get(id=pk)
    form =  UpdateRecordForm(instance=record)
    if request.method=='POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request," update Complete ")
            return redirect('dashboard')
    context={"form":form}
    return render(request,'webapp/update-record.html', context)  


#read single record
@login_required(login_url='my-login')
def single_record(request, pk):
    all_records = customer.objects.get(id=pk)
    context ={"record":all_records}
    return render(request, 'webapp/view-record.html',context=context)


# delete record
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = customer.objects.get(id=pk)
    record.delete()
    messages.success(request,"Data Delete Successfully")
    return redirect("dashboard")


#kunalprajapat
#kunal11115

# logout user
def user_logout(request):
    auth.logout(request)
    messages.success(request,"Log-Out Success")
    return redirect('my-login')

