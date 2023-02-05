from django.urls import path
from .endpoints import PageListAPIView, PageCreateAPIView, \
    PageListCreateAPIView, PageUpdateAPIView, \
    PageRetrieveUpdateAPIView, PageRetrieveDestroyAPIView, \
    PageRetrieveUpdateDestroyAPIView, PagePostListAPIView


urlpatterns = [
    path("page_list/", PageListAPIView.as_view(), name="page_list"),
    path("page_create/", PageCreateAPIView.as_view(), name="page_create"),
    path("page_list_create/", PageListCreateAPIView.as_view(), name="page_list_create"),
    path("page_update/<int:pk>", PageUpdateAPIView.as_view(), name="page_update"),
    path("page_retrieve_update/<int:pk>", PageRetrieveUpdateAPIView.as_view(), name="page_retrieve_update"),
    path("page_retrieve_destroy/<int:pk>", PageRetrieveDestroyAPIView.as_view(), name="page_retrieve_destroy"),
    path("page_retrieve_update_destroy/<int:pk>", PageRetrieveUpdateDestroyAPIView.as_view(), name="page_retrieve_update_destroy"),
    path("page_post_list/", PagePostListAPIView.as_view(), name="page_post_list")


]