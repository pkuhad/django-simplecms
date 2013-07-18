from django.conf.urls.defaults import *

from .views import PageDetailView, PageCreateView

urlpatterns = patterns('cms.pages.views',
    url(r'page/(?P<pk>\d+)/$', PageDetailView.as_view(), name='page-detail'),
    url(r'page/create/$', PageCreateView.as_view(), name='page-create'),
    #url(r'$', 'index', name='page_index'),

)    
 
