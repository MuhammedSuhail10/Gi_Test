from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import csv, io
import os

class ImportLeadsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_csv_import_data(self):
        print("Testing CSV Import Data after file creation")
        csv_content = io.StringIO()
        csv_writer = csv.writer(csv_content)
        csv_writer.writerow(['name', 'email', 'age'])
        csv_writer.writerow(['John Doe', 'john@example.com', '-1'])
        csv_writer.writerow(['John Doe', 'john@example.com', '24'])
        csv_writer.writerow(['Jane Smith', 'jane@example.com', '30'])
        csv_writer.writerow(['Alice Johnson', 'alice@example.com', '28'])
        csv_writer.writerow(['Bob Brown', 'bob@example.com', '35'])
        csv_writer.writerow(['Charlie White', '', '40'])
        csv_content.seek(0)
        csv_file = SimpleUploadedFile("leads.csv", csv_content.getvalue().encode('utf-8'), content_type="text/csv")
        response = self.client.post('/api/user/import_leads', {'file': csv_file}, format='multipart')
        print(response.json())
    
    def test_csv_file_import(self):
        print("Testing CSV File Import")
        csv = './user/asset/user.csv'
        with open(csv, 'rb') as file:
            csv_file = SimpleUploadedFile(name='user.csv', content=file.read(), content_type='text/csv')
        response = self.client.post('/api/user/import_leads', {'file': csv_file}, format='multipart')
        print(response.json())