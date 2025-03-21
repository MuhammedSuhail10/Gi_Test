from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import csv, io
import os

class RateLimitTesting(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_requests_limit(self):
        print("Testing Rate Limiting")
        for i in range(101):
            response = self.client.get('/api/middle/middleware_test')
            print(response.json())