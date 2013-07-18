from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings

from .views import IndexView, PageDetailView, PageCreateView, PageUpdateView
from .decorators import is_superuser

urlpatterns = patterns('cms.pages.views',
    url(r'page/(?P<pk>\d+)/$', PageDetailView.as_view(), name='page-detail'),
    url(r'page/(?P<pk>\d+)/edit$', PageUpdateView.as_view(), name='page-update'),
    url(r'page/create/$', is_superuser(PageCreateView.as_view()), name='page-create'),
    url(r'^$', IndexView.as_view(), name='page-index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
 
