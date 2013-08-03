from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings

from .views import page_list

urlpatterns = patterns('',
    url(r'pages/$', page_list, name='api-page-list'),
)
 
