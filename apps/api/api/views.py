from django.shortcuts import get_object_or_404, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string

from api.models import DroneStatus, DroneType, Customer, CustomerToken


def hello_world(request):
    return JsonResponse({"helloWorld": False})


def get_drone_statuses(request):
    statuses = DroneStatus.objects.all()
    return JsonResponse({"droneStatuses": [status.toJSON() for status in statuses]})


def get_drone_types(request):
    drone_types = DroneType.objects.all()
    return JsonResponse({"droneTypes": [drone_type.toJSON() for drone_type in drone_types]})


@csrf_exempt
def new_customer(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'message': 'POST method required. Do not use these credentials.'})

    # if username taken
    if Customer.objects.filter(pk=request.POST['username']):
        return JsonResponse({'success': False, 'message': 'username taken'})

    Customer(
        username=request.POST['username'],
        password_hash=make_password(request.POST['password']),
        first_name=request.POST['firstName'],
        last_name=request.POST['lastName'],
    ).save()

    return JsonResponse({'success': True})


@csrf_exempt
def customer_login(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'message': 'POST method required.'})

    customers = Customer.objects.filter(pk=request.POST['username'])
    # if querey set is not empty and passwords match
    # susceptible to timing attack
    if not customers or not check_password(request.POST['password'], customers[0].password_hash):
        return JsonResponse({'success': False, 'message': 'bad login'})

    response = JsonResponse({'success': True})
    token = get_random_string(length=128)
    CustomerToken(
        token=token,
        customer=customers[0]
    ).save()
    response.headers["Set-Cookie"] = f"customer-token={token}"

    return response
