from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from blog.models import User

def login(request):
    if request.method == "POST":
        uf = UserFormLogin(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userResult = User.objects.filter(username=username, password=password)
            if (len(userResult) > 0):
                return render_to_response('success.html', {'operation': "登录"})
            else:
                return render_to_response('Fail.html', {'operation': "登录"})
    else:
            uf = UserFormLogin()
    return render_to_response("Userlogin.html", {'uf':uf})

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password1 = forms.CharField(label='密码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')

class UserFormLogin(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())