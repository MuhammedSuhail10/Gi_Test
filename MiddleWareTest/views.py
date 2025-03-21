from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def middleware_test(request):
    return Response({"message": "Request successful!"})