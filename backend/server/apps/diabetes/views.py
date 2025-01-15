from django.shortcuts import render
from . models import Diabetes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def add_sugar(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      fasting_data = data.get('fasting_sugar')
      random_data = data.get('random_sugar')

      diabetes = Diabetes.objects.create(fasting_sugar = fasting_data, random_sugar = random_data)
      diabetes.save() 
      return JsonResponse({"message": "Data has been added successfully"}, status = 200)
    except json.JSONDecodeError:
      return JsonResponse({"error" : "Invalid JSON data"}, status = 400) 
  else:
    return JsonResponse({"error": "Invalid request method"}, status = 405)
  

def list_data(request):
  if request.method == 'GET':
    data = list(Diabetes.objects.values('id', 'fasting_sugar', 'random_sugar', 'created_at'))
    return JsonResponse(data, safe=False)
  else:
    return JsonResponse({'error': "Invalid request method"}, status = 405)