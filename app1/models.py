from django.db import models

# Create your models here.


class Server(models.Model):
    server_name = models.CharField(max_length=20,unique=True)
    server_desc = models.CharField(max_length=200,blank=True)
    server_date_create = models.DateTimeField('date creating')
    server_ip = models.IPAddressField(blank=True)
    def __unicode__(self): 
        return u'%s   %s' % (self.server_name, self.server_ip)

class User(models.Model):
    user_id = models.ForeignKey(Server, on_delete=models.CASCADE) 
    user_name = models.CharField(max_length=20)
    user_desc = models.CharField(max_length=200,blank=True)
    user_enable = models.NullBooleanField(default=True)
    def __unicode__(self):  
        return u'%s  ---  %s' %(self.user_name, self.user_id)

