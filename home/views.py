# Create your views here.
import random
import string
import time

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def home2(request):
    return render(request, 'home2.html')


def sendjson(request):
    n = 3
    source_ip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(
        random.randint(0, 255)) + str(random.randint(0, 255))
    dest_ip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + str(
        random.randint(0, 255))
    protocol = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(n))
    data = {
        "data": [
            {
                "id": "1",
                "source": source_ip,
                "destination": dest_ip,
                "protocol": protocol,
                "info": "This is clean",
                "info2": "This is clean too",
                "info3": "This is clean as well"
            }
        ]
    }
    time.sleep(5)
    return JsonResponse(data)


def sendjson2(request):
    data = {
        "data": [{
            "key1": {"subkey1": "a", "subkey2": "b"},
            "key2": {},
            "key3": "hello KEY3"
        }]
    }
    print("using simple retrieve ", data['data'][0]['key3'])
    # dictionary.get("bogus", default_value) using the default_value will set it to that if value is not found
    print("using get ", data.get('data')[0].get('key3', "default"))
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
