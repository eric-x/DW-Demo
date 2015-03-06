from django.db import models

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'Store: %s@%s'%(self.title, self.address)

class AccessPoint(models.Model):
    store = models.ForeignKey(Store)
    nick = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'AccessPoint: %s@%s'%(self.id, self.store)

class MenuDish(models.Model):
    store = models.ForeignKey(Store)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    
    def __unicode__(self):
        return u'MenuDish: %s@%s'%(self.name, self.store)


