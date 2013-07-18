from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings

from .views import IndexView, PageDetailView, PageCreateView

urlpatterns = patterns('cms.pages.views',
    url(r'page/(?P<pk>\d+)/$', PageDetailView.as_view(), name='page-detail'),
    url(r'page/create/$', PageCreateView.as_view(), name='page-create'),
    url(r'^$', IndexView.as_view(), name='page_index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
 
