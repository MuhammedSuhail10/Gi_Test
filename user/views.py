from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
import csv,io
from .utils.csv_util import csv_fetch
from rest_framework import status

@api_view(['POST'])
def import_leads(request):
    if request.FILES.get('file') and request.FILES.get('file').name.endswith('.csv'):
        text_file = io.TextIOWrapper(request.FILES.get('file'), encoding='utf-8')
        imported, existing, error_data = csv_fetch(text_file)
        return Response({'status':True,'message': 'Extraction Completed','imported_count':imported,'existing_count':existing,'error_data':error_data})
    return Response({'status':False,'message': 'File format not supported'}, status=status.HTTP_200_OK)