from rest_framework import serializers
from .models import Buy, Rent

class BuySerializers(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = '__all__'


class RrntSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'

