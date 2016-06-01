from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# class Resource( models.Model ):
#   '''resources available for purchase'''
#   name = models.CharField( max_length=250 )
#   location = models.CharField( max_length=250 )
#   price = models.DecimalField( decimal_places=2, max_digits=7 )
#
# class Purchase( models.Model ):
#   '''purchases'''
#   resource = models.ForeignKey( Resource )
#   purchaser = models.ForeignKey( User )
#   purchased_at = models.DateTimeField(auto_now_add=True)
#   tx = models.CharField( max_length=250 )

class AboutUs(models.Model):
  text = models.CharField(max_length=250)

class AppsDescription(models.Model):
  iOsTitulo = models.CharField(max_length=250)
  iOsDescripcion = models.CharField(max_length=250)
  androidTitulo = models.CharField(max_length=250)
  androidDescripcion = models.CharField(max_length=250)

class Transection(models.Model):
  money = models.CharField(max_length=250)

class PaypalOption(models.Model):
  pdt_token = models.CharField(max_length=250)
  paypal_email = models.EmailField()
  return_url = models.URLField()
  paypal_url = models.URLField()
  pdt_url = models.URLField()

  def __str__(self):
    return self.pdt_token