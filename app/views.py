from django.shortcuts import render, HttpResponse, redirect
from django import forms
from pyexpat.errors import messages


# Create your views here.
def index(request):
    if request.method == "GET":
       return render(request, "index.html")

    #print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == "111":
         return HttpResponse("登陆成功")
       #return redirect("https://www.runoob.com/python3/python3-basic-syntax.html")
    return render(request, "index.html", {"error_massage": "用户名或密码错误"})
    # return render(request, "index.html")
#class UserModelForm(forms.ModelForm): # 继承内置Modelform模块
# def login(request):
#     if request.method == "GET":
#        return render(request, "login.html")
#
#     #print(request.POST)
#     username = request.POST.get("user")
#     password = request.POST.get("pwd")
#     if username == 'root' and password == "111":
#          return HttpResponse("登陆成功")
#        #return redirect("https://www.runoob.com/python3/python3-basic-syntax.html")
#     return render(request, "login.html",{"error_massage":"用户名或密码错误"})

# def register(request):
#     if request.method == "GET":
#         return render(request, "register.html")
#     username = request.POST.get("user")
#     password = request.POST.get("pwd")
#     password1 = request.POST.get("pwd1")
#     if password != password1:
#         r = messages.error(request, '两次输入的密码不同,请重新输入')
#         print(r)
#         return redirect('register')

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def logout(request):
    return render(request, "logout.html")