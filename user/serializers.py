from rest_framework import serializers
from .models import *

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'age', 'username']