
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data['name']
        password =data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login successful
            return JsonResponse({'success': True})
        else:
            # login failed
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else:
        # method not allowed
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        username = data['username']
        password1 =data['password']
        password2 = data['confirm_password']
        # Extract username field
        if password1 != password2:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        try:
            user = User.objects.create_user(username, password=password1)
            user.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)