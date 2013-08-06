from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PageList, PageDetail

urlpatterns = patterns('',
    url(r'pages/$', PageList.as_view(), name='api-page-list'),
    url(r'pages/(?P<pk>[0-9]+)/$', PageDetail.as_view(), name='api-page-detail'),
)
 
urlpatterns = format_suffix_patterns(urlpatterns)
