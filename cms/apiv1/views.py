from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cms.pages.models import Page
from cms.apiv1.serializers import PageSerializer


@api_view(['GET'])
def page_list(request, format=None):
    """List all pages"""
    
    if request.method == "GET":
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def page_detail(request, pk):

	try:
		page = Page.objects.get(pk=pk)
	except Page.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = PageSerializer(page)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = PageSerializer(page, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		page.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)