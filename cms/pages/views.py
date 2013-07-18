import logging

from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext as _

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .models import Page
from .forms import CreatePageForm

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = "pages/index.html"

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    form_class = CreatePageForm
    model = Page
