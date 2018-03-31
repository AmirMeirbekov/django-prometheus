import os

from django.conf.urls import url
from django_prometheus import exports

url_prefix = ''
if os.getenv('PROMETHEUS_URL_TOKEN'):
    url_prefix = '{}/'.format(os.getenv('PROMETHEUS_URL_TOKEN'))

urlpatterns = [
    url(r'^{}metrics$'.format(url_prefix), exports.ExportToDjangoView,
        name='prometheus-django-metrics'),
]
