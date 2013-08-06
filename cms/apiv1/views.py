from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from cms.pages.models import Page
from cms.apiv1.serializers import PageSerializer


class PageList(APIView):
    """List all pages"""
    
    def get(self, request, format=None):
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
    	serializer = PageSerializer(data=request.DATA)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PageDetail(APIView):
	def get_object(self, pk):
		try:
			return Page.objects.get(pk=pk)
		except Page.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		page = self.get_object(pk)
		serializer = PageSerializer(page)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		page = self.get_object(pk)
		serializer = PageSerializer(page, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		page = self.get_object(pk)
		page.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)