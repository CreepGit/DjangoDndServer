from django.http import JsonResponse, HttpResponse
from rpgsheet.models import CharacterInformation
import json
# Create your views here.

def list_view(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Only get method is permitted'})
    objects = CharacterInformation.objects.values("key","created_at","updated_at")
    return JsonResponse({
        "count": objects.count(),
        "characters": [*objects],
    })

def detail_view(request, key=None):
    if request.method != 'GET':
        return JsonResponse({'error': 'Only get method is permitted'})
    if not key:
        return JsonResponse({'error': 'Key was not set to a value'})
    if len(key) < 5:
        return JsonResponse({'error': 'Key is too short'})
    obj = CharacterInformation.objects.filter(key=key)
    if not obj.exists():
        return JsonResponse({'error': 'No item found with that key'})
    if obj.count() != 1:
        return JsonResponse({'error': 'Multiple values with that key. This should not be possible'})
    
    # Success
    obj = obj.first()
    return JsonResponse({
        "key":obj.key,
        "data":obj.data,
        "created":obj.created_at,
        "modified":obj.updated_at,
    })

def post_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only post method is permitted'})
    body: dict = json.loads(request.body.decode("utf-8"))
    key = body.get("key")
    password = body.get("password")
    data = body.get("data")
    if not key:
        return JsonResponse({'error': 'Key missing'})
    if len(key) < 8:
        return JsonResponse({'error': 'Key is too short'})
    if not password:
        return JsonResponse({'error': 'Password missing'})
    if not data:
        return JsonResponse({'error': 'Character data missing'})
        
    query = CharacterInformation.objects.filter(key=key)
    if query.exists():
        obj = query.first()
        if obj.password != password:
            return JsonResponse({'error': 'Password does not match'})
        obj.data = data
        obj.save()
    else:
        CharacterInformation.objects.create(
            key=key,
            password=password,
            data=data,
        )
    return JsonResponse({'ok': 'ok'})


