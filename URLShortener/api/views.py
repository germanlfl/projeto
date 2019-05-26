from django.shortcuts import render,redirect
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from rest_framework import  viewsets
from rest_framework.response import Response
from . import models
from . import serializers
import time
import sys
# Create your views here.

class ShortUrlViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ShortUrlSerializer
    queryset = models.ShortUrl.objects.all()

    def create(self,request):

        start = time.time()

        try:
            seriaT = serializers.ShortUrlSerializer(data=request.data)
            seriaT.is_valid(raise_exception=True)
            objeto = seriaT.save()
        except ValidationError as e:
           if 'unique' in str(e.detail):
                return Response({'alias':request.data.get('alias'),'ERR_CODE':'002','DESCRIPTION':'CUSTOM ALIAS ALREADY EXIST'})
           return Response({'mensagem':'INSERT A VALID URL'})

        return Response({'alias': objeto.alias ,'url': request.get_host() +'/'+objeto.alias, 'statistics': {'time':str(round((time.time() - start) * 1000)) + 'ms'}})

    def retrieve(self, request, pk=None):
        

        try:    
            url = models.ShortUrl.objects.get(pk=pk)
        except:
            return Response({'ERR_CODE':'002','description':'SHORTENED URL NOT FOUND'})

        url.access()
        redirectUrl = url.url

        if(redirectUrl != 'http'):
            redirectUrl = 'http://'+redirectUrl
        return redirect(redirectUrl)
    
def index(request):
    return render(request,'api/index.html')
