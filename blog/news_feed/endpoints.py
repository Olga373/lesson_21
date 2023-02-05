from rest_framework.generics import \
    (ListAPIView, CreateAPIView,
    RetrieveAPIView, UpdateAPIView, DestroyAPIView,\
    RetrieveUpdateAPIView, RetrieveDestroyAPIView,\
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, \
    )

from rest_framework import permissions

from .models import Page, Post
from .serializers import PageSerializer, PostSerializer, PagePostSerializer
from itertools import chain

class PageListAPIView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageCreateAPIView(CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer



class PageListCreateAPIView(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageUpdateAPIView(UpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PagePostListAPIView(ListAPIView):
    serializer_class = PagePostSerializer

    def get_queryset(self):
        post_queryset = Post.objects.all()
        page_queryset = Page.objects.all()
        queryset = list(chain(set(page_queryset), set(post_queryset)))
        queryset.sort(key=lambda instance: instance.pk)
        return queryset
