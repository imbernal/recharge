import requests
import time

# Create your views here.
from app import models
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .models import *

from app import paypal_trans


def homepage(request):
    paypal_option = PaypalOption.objects.get(pk=1)
    appDescription = AppsDescription.objects.get(pk=1)
    about_us = AboutUs.objects.get(pk=1)

    # if request.method == 'POST':
    #     provider = request.POST['_provider']
    #     phone = request.POST['_phone']
    #     monto = request.POST['_curr']
    #     purchased(provider, phone, monto)

    # r = requests.get('https://prod01.midas-card.com/plataforma/ws2/Balance.midas?parametros=/')
    return render(request, 'app/index.html',
                  {'paypal_url': paypal_option.paypal_url, 'paypal_email': paypal_option.paypal_email,
                   'paypal_return_url': paypal_option.return_url, 'about_us': about_us,
                   'appDescription': appDescription})


@csrf_exempt
def save_data(request):
    provider = request.POST['provider']
    phone = request.POST['phone']
    amount = request.POST['amount']
    item_number = request.POST['item_number']

    trans = Transaction()
    trans.money = amount
    trans.phone = phone
    trans.provider = provider
    trans.item_number = item_number

    trans.save()

    return HttpResponse(200)


def purchased(request):
    # resource = get_object_or_404(models.Resource, pk=id)
    # user = get_object_or_404(User, pk=id)
    resultText = ''
    if request.REQUEST.has_key('tx'):

        # tx = request.REQUEST['tx']

        # result = paypal_trans.Verify(tx)

        # if result.success():  # valid
        item_number = request.GET['item_number']


        trans = Transaction.objects.get(item_number=item_number)


        urlPost = settings.MIDAS_URL + trans.provider + '.midas?parametros=' + 'punto54-' + str(
            trans.id) + '/' + settings.MIDAS_USER_ID + '/' + settings.MIDAS_PASSWORD + '/' + str(trans.phone) + '/' + str(
            trans.money)

        try:
            r = requests.get(urlPost, timeout=46)

            result = r.text.split('/')
            resultText = result[1]
            notif = Notification()
            notif.message = result[1]
            notif.save()

        except Exception:

            urlPost = settings.MIDAS_URL + 'Verificacion.midas?parametros=' + 'punto54-' + str(
                trans.id) + '/' + settings.MIDAS_USER_ID + '/' + settings.MIDAS_PASSWORD

            try:

                requests.get(urlPost, timeout=10)

            except Exception:

                # si la verificacion se demora 10 segundo hago 3 anulaciones
                for i in range(1, 5):
                    urlPost = settings.MIDAS_URL + 'Reverso.midas?parametros=' + 'punto54-' + str(
                        trans.id) + '/' + settings.MIDAS_USER_ID + '/' + settings.MIDAS_PASSWORD

                    requests.get(urlPost)

                    time.sleep(10)

                # else:  # didn't validate
                #     return render_to_response('error.html', {'error': "Failed to validate payment"},
                #                               context_instance=RequestContext(request))
    else:  # no tx
        return render_to_response('error.html', {'error': resultText},
                                  context_instance=RequestContext(request))

        # return render_to_response('error.html', {'error': "Error"},
        #                           context_instance=RequestContext(request))

        # def api_request(request):
        # provider = request.POST['_provider']
        # phone = request.POST['_phone']
        # monto = request.POST['_curr']
        #
        # trans = Transection()
        # trans.money = monto
        # trans.save()
        #
        # urlPost = settings.MIDAS_URL + provider + '.midas?parametros=' + 'punto54-' + str(
        #     trans.id) + '/' + settings.MIDAS_USER_ID + '/' + settings.MIDAS_PASSWORD + '/' + str(phone) + '/' + str(monto)
        #
        # r = requests.get(urlPost, timeout=46)
        #
        # requestTime = r.elapsed.total_seconds()
        #
        # resultText = ''
        #
        # if requestTime > 45:
        #
        #     urlPost = settings.MIDAS_URL + 'Verificacion.midas?parametros=' + 'punto54-' + str(
        #         trans.id) + '/' + settings.MIDAS_USER_ID + '/' + settings.MIDAS_PASSWORD
        #
        #     r = requests.get(urlPost)
        #
        #     requestTime = r.elapsed.total_seconds()
        #
        #     if requestTime > 10:  # si la verificacion se demora 10 segundo hago 3 anulaciones
        #         for i in range(1, 5):
        #             urlPost = settings.MIDAS_URL + 'Reverso.midas?parametros=' + 'punto54-' + str(
        #                 trans.id) + '/' + settings.MIDAS_USER_ID + '/' + settings.MIDAS_PASSWORD
        #
        #             r = requests.get(urlPost)
        #
        #             result = r.text.split('/')
        #
        #             resultText = result[1]
        #
        #             time.sleep(10)
        #     else:
        #         result = r.text.split('/')
        #         resultText = result[1]
        #
        # else:
        #     result = r.text.split('/')
        #     resultText = result[1]
        #
        #     if result[0] == '00':
        #         return redirect(reverse('home'))
        #
    return render_to_response('error.html', {'error': resultText},
                              context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))
