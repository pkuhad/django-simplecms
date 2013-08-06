from rest_framework import status
from rest_framework import mixins, generics

from cms.pages.models import Page
from cms.apiv1.serializers import PageSerializer, UserSerializer

from django.contrib.auth.models import User

class PageList(generics.ListCreateAPIView):
    """List all pages"""
    
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Page.objects.all()
	serializer_class = PageSerializer

class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

