# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def home2(request):
    return render(request, 'home2.html')


def sendjson(request):
    data = {
        "data": [
            {
                "id": "1",
                "source": "192.168.1.2",
                "destination": "192.168.1.4",
                "protocol": "TCP",
                "info": "This is clean",
                "info2": "This is clean too",
                "info3": "This is clean as well"
            },
            {
                "id": "1",
                "source": "192.168.1.2",
                "destination": "192.168.1.4",
                "protocol": "TCP",
                "info": "This is clean",
                "info2": "This is clean too",
                "info3": "This is clean as well"
            },
            {
                "id": "3",
                "source": "192.168.1.2",
                "destination": "192.168.1.4",
                "protocol": "TCP",
                "info": "This is clean",
                "info2": "This is clean too",
                "info3": "This is clean as well"
            },
            {
                "id": "4",
                "source": "192.168.1.2",
                "destination": "192.168.1.4",
                "protocol": "TCP",
                "info": "This is clean",
                "info2": "This is clean too",
                "info3": "This is clean as well"
            },
            {
                "id": "5",
                "source": "192.168.1.2",
                "destination": "192.168.1.4",
                "protocol": "TCP",
                "info": "This is clean",
                "info2": "This is clean too",
                "info3": "This is clean as well"
            },
            {
                "id": "6",
                "source": "192.168.1.2",
                "destination": "192.168.1.4",
                "protocol": "TCP",
                "info": "This is clean",
                "info2": "This is clean too",
                "info3": "This is clean as well"
            },
        ]
    }
    return JsonResponse(data)


def sendjson2(request):
    data = {
        "data": [{
            "key1": {"subkey1": "a", "subkey2": "b"},
            "key2:": {},
            "key3": "hello KEY3"
        }]
    }
    print("using simple retrieve ", data['data'][0]['key3'])
    # dictionary.get("bogus", default_value) using the default_value will set it to that if value is not found
    print("using get ", data.get('data')[0].get('key3', "default"))
    return JsonResponse(data)
