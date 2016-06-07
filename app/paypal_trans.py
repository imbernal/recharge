import decimal
import json
import urllib.request
import requests
import sys

from django.conf import settings

from app.models import PaypalOption
from requests.packages import urllib3


class Verify(object):
    '''builds result, results, response'''
    def __init__(self, tx):
        paypal = PaypalOption.objects.get(pk=1)
        # transaction =  app.models.Purchase.objects.get( tx=tx )
        self.result = 'Transaction %s has already been processed' % tx
        self.response = self.result

        post = dict()
        post['cmd'] = '_notify-synch'
        post['tx'] = tx
        post['at'] = paypal.pdt_token
        try:
            self.response = requests.post(paypal.pdt_url, data=json.dumps(post), verify=False).text
        except Exception:
            pass


        lines = self.response.split('\n')
        print(lines)
        print(self.response)
        self.result = lines[0].strip()
        print(self.result)
        self.results = dict()
        for line in lines[1:]:  # skip first line
            linesplit = line.split('=', 2)
            # if len(linesplit) == 2:
            #     self.results[linesplit[0].strip()] = urllib.unquote(linesplit[1].strip())


    def success(self):
        return self.result == 'SUCCESS' and self.results['payment_status'] == 'Completed'

    def amount(self):
        return decimal.Decimal(self.results['payment_gross'])
