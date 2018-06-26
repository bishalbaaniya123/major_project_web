# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render


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
    data = {
        "isStart": False
    }
    return JsonResponse(data)
