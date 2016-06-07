from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from swampdragon.models import SelfPublishModel
from .serializers import NotificationSerializer


class Notification(SelfPublishModel, models.Model):
    serializer_class = NotificationSerializer
    message = models.TextField()

    def __str__(self):
        return self.message

class AboutUs(models.Model):
    text = models.CharField(max_length=250)


class AppsDescription(models.Model):
    iOsTitulo = models.CharField(max_length=250)
    iOsDescripcion = models.CharField(max_length=250)
    androidTitulo = models.CharField(max_length=250)
    androidDescripcion = models.CharField(max_length=250)


class Transaction(models.Model):
    money = models.CharField(max_length=250)
    provider = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    item_number = models.CharField(max_length=255)

    def __str__(self):
        return self.phone


class PaypalOption(models.Model):
    pdt_token = models.CharField(max_length=250)
    paypal_email = models.EmailField()
    return_url = models.URLField()
    paypal_url = models.URLField()
    pdt_url = models.URLField()

    def __str__(self):
        return self.pdt_token
