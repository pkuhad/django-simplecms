import logging

from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Page

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello World")

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
