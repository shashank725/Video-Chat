from django.shortcuts import render, redirect
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages                           #Flash messages
from django.contrib.auth import authenticate, login, logout   #Authentication
from django.contrib.auth.decorators import login_required     #Login required decorator
from .forms import CreateUserForm
import random


# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')          #Way of accessing form data
                messages.success(request, 'Account created successfully' + user)  #Flash messages

                return redirect('login')
        context = {'form':form}
        return render(request, 'base/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')               #Another way of accessing form data
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            # if user:
            #     login(request, user)
            #     return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login')
def lobby(request):
    randomNo = random.randint(1, 100)
    # print(request.user))
    # code = request.user + str(randomNo)
    print(randomNo)
    return render(request, 'base/lobby.html', context={'randomNo':randomNo})

@login_required(login_url='/login')
def room(request):
    return render(request, 'base/room.html')


def getToken(request):
    # appId = "YOUR APP ID"
    appId = "9cf5effbdaf94ecda01d8c98ff167e3b"
    # appCertificate = "YOUR APP CERTIFICATE"
    appCertificate = "d57d793a5e454fd0a45cb7d35815b89c"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)