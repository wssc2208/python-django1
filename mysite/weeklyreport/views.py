from django.shortcuts import render
from django import forms

from django.shortcuts import render, render_to_response

from django.http import HttpResponseRedirect

from weeklyreport.models import weeklyUser

import datetime
now = datetime.datetime.now()


# Create your views here.
def login(request):
    if request.method == "POST":
        uf = UserLoginForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            request.session['username'] = username
            userResult = weeklyUser.objects.filter(username=username, password=password)
            if(len(userResult)>0):
                return HttpResponseRedirect('/successful/')
            else:
                return render_to_response('unsuccessful.html', {'username':uf.cleaned_data['username'], 'operation': "登录"})
    else:
            uf = UserLoginForm()
    return render_to_response("login.html", {'uf':uf})

def successful(request):
    username = request.session.get('username')
    return render_to_response('successful.html', {'username': username,
                                                  'operation': "登录",
                                                  'refresh_url': '/reportcontent.html'})

# 注册界面，暂时停止开发
# def regist(request):
#     if request.method == "POST":
#         uf = UserRegistForm(request.POST)
#         if uf.is_valid():
#             username = uf.cleaned_data['username']
#             password1 = uf.cleaned_data['password1']
#             password2 = uf.cleaned_data['password2']
#             if password1 == password2:
#                 pass
#             else:
#                 return render_to_response('unsuccessful.html', {'operation': "注册"})

def weeklyContent(request):
    username = request.session.get('username')
    if request.method == "POST":
        weeklyReportContent = weeklyReportContentForm(request.POST)
        if weeklyReportContent.is_valid():

    else:
        weeklyReportContent = weeklyReportContentForm()
    return render_to_response('reportcontent.html', {'username': username,
                                                     'reporttime': now,
                                                     'content': weeklyReportContent})


class UserLoginForm(forms.Form):
    username = forms.CharField(label= "用户名", max_length=50)
    password = forms.CharField(label= "密码", widget = forms.PasswordInput())

class UserRegistForm(forms.Form):
    username = forms.CharField(label = "用户名", max_length = 50)
    password1 = forms.CharField(label="输入密码", widget = forms.PasswordInput())
    password2 = forms.CharField(label="再次输入密码", widget = forms.PasswordInput())

class weeklyReportContentForm(forms.Form):
    update_content  = forms.CharField(label = "内容", widget=forms.Textarea())