import logging

from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext as _

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, ListView

from .models import Page
from .forms import CreatePageForm

logger = logging.getLogger(__name__)


class IndexView(ListView):
    model = Page
    template_name = "pages/index.html"
    paginate_by = 5

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    form_class = CreatePageForm
    model = Page

class PageUpdateView(UpdateView):
    form_class = CreatePageForm
    model = Page

class PhotostreamView(ListView):
    template_name = "pages/photostream.html"
    queryset = Page.objects.all()


