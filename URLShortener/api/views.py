from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework import  viewsets
from rest_framework.response import Response
from . import models
from . import serializers
import time
# Create your views here.

class ShortUrlViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ShortUrlSerializer
    queryset = models.ShortUrl.objects.all()

    def create(self,request):

        start = time.time()

        if(request.data == '' and request.query_params == ''):
            return Response()
        try:
            seriaT = serializers.ShortUrlSerializer(data=request.data)
            seriaT.is_valid(raise_exception=True)
        except:
            return Response({'mensagem':'INSERT A VALID URL'})
        objeto = seriaT.save()

        return Response({'alias': objeto.alias ,'url': request.get_host() +'/'+objeto.alias, 'statistics': {'time':str(round((time.time() - start) * 1000)) + 'ms'}})

    def retrieve(self, request, pk=None):
        
        try:
            url = models.ShortUrl.objects.get(pk=pk)
            url.count+=1
            url.access()
        except:
            return (Response({'ERR_CODE':'002','description':'SHORTENED URL NOT FOUND'}))
        redirectUrl = url.url

        if(redirectUrl != 'http'):
            redirectUrl = 'http://'+redirectUrl
        return redirect(redirectUrl)
    
def index(request):
    return HttpResponse('')
