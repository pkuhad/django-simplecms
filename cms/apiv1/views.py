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

@csrf_exempt
def page_detail(request, pk):

	try:
		page = Page.objects.get(pk=pk)
	except Page.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = PageSerializer(page)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = PageSerializer(page, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		else:
			return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		page.delete()
		return HttpResponse(status=204)