# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
import random


def home(request):
    return render(request, 'index.html')


def dateRange(request):
    return render(request, 'dateRange.html')


def sendjson(request):
    data = [
        [
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
            },
        ],
        100
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


id_no = 0


def get_flows(request):
    time = request.GET.get('time')
    page_no = request.GET.get('page_no')
    per_page = request.GET.get('per_page')
    print("get_flows", time, page_no, per_page)
    global id_no
    id_no = id_no + 1

    data = [
        [
            {
                "id": "1",
                "recorded_time": 1529864806.5679667,
                "flow_source": "192.168.0.101",
                "flow_destination": "104.120.84.173",
                "type": "Malignant",
                "start_time": 1529864805.376709
            },
            {
                "id": "1",
                "recorded_time": 1529864806.5679667,
                "flow_source": "192.168.0.210",
                "flow_destination": "104.120.84.173",
                "type": "Malignant",
                "start_time": 1529864805.376709
            }
        ],
        [
            {
                "id": "1",
                "recorded_time": 1529864806.5679667,
                "flow_source": "192.168.0.210",
                "flow_destination": "104.120.84.173",
                "type": "Benign",
                "start_time": 1529864805.376709
            },
            {
                "id": "1",
                "recorded_time": 1529864806.5679667,
                "flow_source": "192.168.0.210",
                "flow_destination": "104.120.84.173",
                "type": "Benign",
                "start_time": 1529864805.376709
            }
        ]

    ]
    return JsonResponse(data, safe=False)


def not_count(request):
    global id_no
    id_no = id_no + 1

    data = {
        "count": id_no,
    }

    return JsonResponse(data, safe=False)


def get_flows_page1(request):
    time = request.GET.get('time')
    page_no = request.GET.get('page_no')
    per_page = request.GET.get('per_page')
    print("get_flows", time, page_no, per_page)
    global id_no
    id_no = id_no + 1

    data = [
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0.210",
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        }
    ]
    return JsonResponse(data, safe=False)


def get_flows_page2(request):
    time = request.GET.get('time')
    page_no = request.GET.get('page_no')
    per_page = request.GET.get('per_page')
    print("get_flows", time, page_no, per_page)
    global id_no
    id_no = id_no + 1

    data = [
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        },
        {
            "id": id_no,
            "recorded_time": 1529864806.5679667,
            "flow_source": "192.168.0." + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            "flow_destination": "104.120.84.173",
            "type": random.choice(["Benign", "Malignant"]),
            "start_time": 1529864805.376709
        }
    ]
    return JsonResponse(data, safe=False)


def send_command_service(request):
    data = {
        'serverRunning': True
    }
    return JsonResponse(data, safe=False)
