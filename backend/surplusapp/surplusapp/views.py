# from django.template import Template
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import SourceInfo, DistributorInfo, Listings
from django.views.decorators.csrf import csrf_exempt,  ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import sys
sys.path.append('..')



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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie

# @ensure_csrf_cookie
@require_POST
@csrf_exempt
def add_listing(request):
    if request.method == 'POST':
        try:
            source_id = 8
            data = json.loads(request.body.decode('utf-8'))  # Parse JSON data from the request body

            # Extract data from the JSON object
            quantity = data.get('quantity')
            food_type = data.get('food_type')
            description = data.get('description')

            # Create a new Listings object using create()
            listing = Listings.objects.create(
                source_id=source_id,  # Assuming source_id is the field name
                quantity=quantity,
                food_type=food_type,
                description=description
            )

            return JsonResponse({'message': 'Listing added successfully!'})
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=400)

    return JsonResponse({'message': 'Invalid request method.'}, status=405)


@csrf_exempt
def get_card_data(request):
    if request.method == 'POST':
        try:
            # Parse the request body as JSON
            data = json.loads(request.body)

            # Extract the source_id from the JSON data
            source_id = data.get('source_id')

            if source_id is not None:
                # Retrieve the source information and related listings for the specified source_id
                source_data = SourceInfo.objects.filter(id=source_id).prefetch_related('listings').values(
                    'name', 'address', 'region', 'phoneno', 'email', 'ratings',
                    'listings__quantity', 'listings__food_type', 'listings__description'
                )

                if source_data:
                    # Convert the query result to a list of dictionaries
                    source_and_listings = list(source_data)
                    return JsonResponse(source_and_listings, safe=False)  # safe=False allows returning a list

                return JsonResponse({"message": "Source not found."}, status=404)
            else:
                return JsonResponse({"message": "Invalid request data. source_id is missing."}, status=400)
        except Exception as e:
            return JsonResponse({"message": f"Error: {str(e)}"}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method."}, status=405)



def sourceloginpage(request):
    return render(request, "slogin.html")

def disloginpage(request):
    return render(request, "dlogin.html")

@api_view(['POST'])
@csrf_exempt
def usrlogin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    http_request = request._request
    try:
        user = authenticate(http_request, username=username, password=password)
        if user is not None:
            login(http_request, user)
            user_data = {
                'username': user.username,
            }        
            response_content = {
                'message': 'Success!1!',
                'user': user_data
            }
            return HttpResponse(content=str(response_content), content_type='application/json', status=200)
        else:
            return HttpResponse(content='{"message": "Invalid Credentials"}', content_type='application/json', status=401)
    except Exception as e:
        return HttpResponse(content='{"message": "500: INTERNAL SERVER ERROR", "error": "' + str(e) + '"}', content_type='application/json', status=500)

@login_required
def ch_auth(request):
    # If the code reaches this point, it means the user is authenticated
    pass



@login_required
class check_auth(APIView):

    def get(self, request, format=None):
        user = request.user
        user_data = {
            'username': user.username,
        }

        return Response({
            'message': 'Authenticated',
            'user': user_data
        })
            


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