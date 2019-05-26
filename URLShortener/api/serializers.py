from api.models import ShortUrl
from rest_framework import serializers

class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ('alias','domain','url','count','created')
