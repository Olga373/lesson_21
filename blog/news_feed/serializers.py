from rest_framework.serializers import ModelSerializer
from .models import Page, Post


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"