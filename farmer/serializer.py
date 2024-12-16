from rest_framework import serializers
from .models import Farmerdata

class farmerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Farmerdata
        fields = "__all__"