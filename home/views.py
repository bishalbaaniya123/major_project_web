# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
import random


def home(request):
    return render(request, 'index.html')


def sendjson(request):
    data = [
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        },
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        },
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        },
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        },
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        },
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        },
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        },
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        },
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        },
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        }
    ]
    return JsonResponse(data, safe=False)


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


def checkServer(request):
    randBool = random.choice([True, False])
    print("This is checkserver")

    data = {
        "isStart": randBool
    }


def checkServerStatus(request):
    randBool = random.choice([True, False])
    print("This is checkserver")

    data = {
        "isStart": randBool
    }
    return JsonResponse(data)


def checkIdle(request):
    message = "User is idle"

    data = {
        "message": message
    }
    return JsonResponse(data)


def get_flows(request):
    time = request.GET.get('time')
    page_no = request.GET.get('page_no')
    per_page = request.GET.get('per_page')
    print("get_flows", time, page_no, per_page)

    data = [
        {
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.105",
            "flow_destination": "104.120.84.173",
            "type": "BENIGN",
            "start_time": 1529864805.376709
        }
    ]
    return JsonResponse(data, safe=False)
