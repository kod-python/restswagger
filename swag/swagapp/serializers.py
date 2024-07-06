from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'quantity', 'created', 'updated']
         
        def get_photo_url(self,obj):
             request = self.context.get('request')
             photo_url = obj.fingerprint.url
             return request.build.absolute_uri(photo_url)