import requests

# Create your views here.
from app import models
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from .models import PaypalOption
import paypal


def homepage(request):
    paypal_option = PaypalOption.objects.get(pk=1)
    # r = requests.get('https://prod01.midas-card.com/plataforma/ws2/Balance.midas?parametros=/')
    return render(request, 'app/index.html', {'paypal_url': paypal_option.paypal_url, 'paypal_email': paypal_option.paypal_email,
                                              'paypal_return_url': paypal_option.return_url})

def purchased(request):
    # resource = get_object_or_404( models.Resource, pk=id )
    # user = get_object_or_404( User, pk=uid )
    if request.REQUEST.has_key('tx'):
        tx = request.REQUEST['tx']

        result = paypal.Verify(tx)
        if result.success():  # valid
            #   todo: incorpporar uso de la api de midas
            return redirect(reverse('home'))
        else:  # didn't validate
            return render_to_response('error.html', {'error': "Failed to validate payment"},
                                      context_instance=RequestContext(request))
    else:  # no tx
        return render_to_response('error.html', {'error': "No transaction specified"}, context_instance=RequestContext(request))
