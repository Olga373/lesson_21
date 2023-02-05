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

class PagePostSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"

    def to_representation(self, instance):
        match isinstance(instance, Post):
            case True:
                serializer = PostSerializer(instance)
            case False:
                serializer = PageSerializer(instance)
            case _:
                raise Exception("Nothing to serialize")
        return serializer.data
