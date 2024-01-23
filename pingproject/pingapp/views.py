# pingapp/views.py
import subprocess
from django.shortcuts import render
from django.http import JsonResponse

def ping(request):
    ip_address = '10.0.5.11'  # Cambia esto con la dirección IP que quieras pinguear
    try:
        subprocess.check_output(['ping', '-t', '5', ip_address])
        response = {'status': 'success', 'message': 'Ping exitoso'}
    except subprocess.CalledProcessError:
        response = {'status': 'error', 'message': 'El ping no tuvo éxito'}
    return JsonResponse(response)
