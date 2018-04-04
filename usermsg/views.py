from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import user
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django import forms


# class UserForm(forms.Form):
#     # username = forms.CharField(label='用户名',max_length=50)
#     # password = forms.CharField(label='密码',widget=forms.PasswordInput())
#     # email = forms.EmailField(label='邮箱')

def user_msg(request):
    name=request.POST['name']
    password=request.POST['password']

def signin(request):

    return render(request, 'usermsg/login.html')

def login(request):

    name=request.POST['name']
    password=request.POST['password']
    user_msg=user.objects.filter(name=name,password=password)

    if user_msg:
        return render(request, 'usermsg/user_msg.html', {'user': user_msg})
    else:
        return HttpResponse('用户名或密码错误,请重新登录')  # 这里最好改成ajax来处理会方便很多


def user_msg_change(request,user_id):
    user_msg = get_object_or_404(user, pk=user_id)
    name = request.POST['name']
    email = request.POST['email']


    user_msg.name=name
    user_msg.email=email

    user_msg.save()

    return HttpResponse("You're change succeed %s." % name)
