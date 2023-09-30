# from django.template import Template
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import SourceInfo, DistributorInfo
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
import json

def reg_signup_view(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username, password=password)
            dist_group = Group.objects.get(name='distributors')
            user.groups.add(dist_group)
            DistributorInfo.objects.create(user=user, name=request.POST['name'], address=request.POST['address'], phoneno=request.POST['phoneno'], email=request.POST['email'])
            user = authenticate(request, username=username, password=password)
            if user:
                return redirect(disloginpage)
        except:
            return JsonResponse({
                'message':'failure'
            },
            status=500
            )
    return render(request, 'distriregpage.html')


def source_signup_view(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username, password=password)
            source_group = Group.objects.get(name='sources')
            user.groups.add(source_group)
            SourceInfo.objects.create(user=user, name=request.POST['name'], address=request.POST['address'], region=request.POST['region'], phoneno=request.POST['phoneno'], email=request.POST['email'])
            user = authenticate(request, username=username, password=password)
            if user:
                return redirect(sourceloginpage)
        except:
            return JsonResponse({
                'message':'failure'
            },
            status=500
            )
    return render(request, 'soureregpage.html')

@csrf_exempt
def source_signup_view2(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            user = User.objects.create_user(username=username, password=password)
            source_group = Group.objects.get(name='sources')
            user.groups.add(source_group)
            SourceInfo.objects.create(
                user=user,
                name=data['name'],
                address=data['address'],
                region=data['region'],
                phoneno=data['phoneno'],
                email=data['email']
            )
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'message': 'Registration successful'}, status=201)
            else:
                return JsonResponse({'error': 'Authentication failed'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def successpage(request):
    return HttpResponse('success signup.')

def homepage(request):
    return render(request, 'homepage.html')


def sourceloginpage(request):
    return render(request, "slogin.html")

def disloginpage(request):
    return render(request, "dlogin.html")

@api_view(['POST'])
@csrf_exempt
def login(request):
    # type=request.data.get('type')
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user=authenticate(request, username=username, password=password)
        if user is not None:
            return JsonResponse({
                "message":"Success!1",
                "username":f"{username}"},
                status=200)
        else:
            return JsonResponse({
                "message":"Invalid Credentials"
                },
                status=401
                )
    except:
        return HttpResponse("500: INTERNAL SERVER ERROR")
def regisource(request):
    return render(request, "soureregpage.html")

def regidist(request):
    return render(request, "distriregpage.html")

def dishome(request):
    return HttpResponse("Distributor Home Page")

def souhome(request):
    return HttpResponse("Source Home Page")

def debugall(request):
    source_info = SourceInfo.objects.all()
    distributor_info = DistributorInfo.objects.all()
    userss=User.objects.values('username')
    passs=User.objects.values('password')
    
    response_data = {
        'source_info': list(source_info.values()),
        'distributor_info': list(distributor_info.values()),
        'users':list(userss),
        'passwors':list(passs),
    }
    
    # Return the data as JSON response
    return JsonResponse(response_data, safe=False)



def chkusername(request):
    username = request.GET.get('username', None)
    data = {
        'exists': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)