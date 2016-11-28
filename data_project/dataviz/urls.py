from django.conf.urls import url
from dataviz.views import SimpleDataView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^data.csv', SimpleDataView.as_view(), ),
    url(r'^$', TemplateView.as_view(template_name='home.html') )
    ]

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)
