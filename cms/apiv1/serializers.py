from cms.pages.models import Page
from rest_framework import serializers

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
