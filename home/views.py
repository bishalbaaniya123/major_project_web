# Create your views here.
import random
import string
import time

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def sendjson(request):
    n = 3
    source_ip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(
        random.randint(0, 255)) + str(random.randint(0, 255))
    dest_ip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + str(
        random.randint(0, 255))
    protocol = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(n))
    info = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(20))
    info2 = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(20))
    info3 = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(20))
    data = {
        "data": [
            {
                "id": random.randint(0, 10000),
                "source": source_ip,
                "destination": dest_ip,
                "protocol": protocol,
                "date": randomDate("1/1/2017 1:30 PM", "1/1/2018 4:50 AM", random.random()),
                "info": info,
                "info2": info2,
                "info3": info3
            }
        ]
    }
    time.sleep(5)
    return JsonResponse(data)


def startfunction(request):
    data = {
        "msg": "You can start now"
    }
    return JsonResponse(data)


def endfunction(request):
    data = {
        "msg": "Process terminated"
    }
    return JsonResponse(data)


def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)
