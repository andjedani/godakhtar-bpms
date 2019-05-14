import datetime
import json
import os
from customers import models,serializers
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects
    serializer_class = serializers.CustomerSerializer

    def initial(self, request, *args, **kwargs):
        log_data = {
            'timestamp': datetime.datetime.now().timestamp()
            'user': request.user.pk,
            'remote_address': request.META['REMOTE_ADDR'],
            'request_method': request.method,
            'request_path': request.get_full_path(),
            'request_body': request.data ,
            'request_query_params': request.query_params ,
            'request_auth': request.auth,
        }
        if not os.path.exists('log'):
            os.makedirs('log')

        with open('log/log.json', 'a+') as f:
            json.dump(log_data, f, sort_keys=True, indent=4)
        viewsets.ModelViewSet.initial(self, request, *args, **kwargs)

