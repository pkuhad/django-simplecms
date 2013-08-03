from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from cms.pages.models import Page
from cms.apiv1.serializers import PageSerializer

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def page_list(request):
    """List all pages"""
    
    if request.method == "GET":
        pages = Page.objects.all()
        serializer = PageSerializer(pages)
        return JSONResponse(serializer.data)

