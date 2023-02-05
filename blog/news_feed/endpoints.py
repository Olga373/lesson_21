from rest_framework.generics import \
    (ListAPIView, CreateAPIView,
    RetrieveAPIView, UpdateAPIView, DestroyAPIView,\
    RetrieveUpdateAPIView, RetrieveDestroyAPIView,\
    RetrieveUpdateDestroyAPIView, ListCreateAPIView)

from rest_framework import permissions

from .models import Page, Post
from .serializers import PageSerializer, PostSerializer


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