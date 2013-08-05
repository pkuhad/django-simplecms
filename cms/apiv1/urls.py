from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings

from .views import page_list, page_detail

urlpatterns = patterns('',
    url(r'pages/$', page_list, name='api-page-list'),
    url(r'pages/(?P<pk>[0-9]+)/$', page_detail, name='api-page-detail'),
)
 
