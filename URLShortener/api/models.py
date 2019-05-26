from django.db import models
import tldextract
import hashlib
import time
# Create your models here.

class ShortUrl(models.Model):
    alias = models.SlugField(max_length=255,primary_key=True,blank=True)
    domain = models.CharField(max_length=255,blank=True)
    url = models.CharField(max_length=255)
    count= models.BigIntegerField(default=0,blank=True,)
    created = models.DateTimeField(auto_now_add=True,blank=True)

    def save(self, *args, **kwargs):

        if(self.alias == ''):
            hash = hashlib.sha1()
            string = str(time.time())+self.url
            hash.update(string.encode())
            self.alias = hash.hexdigest()[:8]

        urlList = tldextract.extract(self.url)
        print(urlList)
        self.domain = urlList.domain + '.' + urlList.suffix
        super(ShortUrl,self).save(*args, **kwargs)

    def access(self, *args, **kwargs):
        self.count +=1
        super(ShortUrl,self).save(*args, **kwargs)

    class Meta:
        ordering = ['-count']