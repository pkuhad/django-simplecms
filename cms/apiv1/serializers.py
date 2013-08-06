from cms.pages.models import Page
from rest_framework import serializers
from django.contrib.auth.models import User

class PageSerializer(serializers.ModelSerializer):
    created_by = serializers.Field(source='created_by.username')

    class Meta:
        model = Page

class UserSerializer(serializers.ModelSerializer):
	pages = serializers.PrimaryKeyRelatedField(many=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'pages')
