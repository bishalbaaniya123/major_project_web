# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


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
