from rest_framework import serializers
from myapp.models import ORDER

class myappSerializer(serializers.ModelSerializer):
    class Meta:
        model = ORDER
        fields = '__all__'