from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PageList, PageDetail, UserList, UserDetail, api_root

urlpatterns = patterns('',
    url(r'/pages/$', PageList.as_view(), name='api-page-list'),
    url(r'/pages/(?P<pk>[0-9]+)/$', PageDetail.as_view(), name='api-page-detail'),
    url(r'/users/$', UserList.as_view(), name='user-list'),
    url(r'/users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'/$', api_root, name='api-root'),
)
 
urlpatterns = format_suffix_patterns(urlpatterns)
