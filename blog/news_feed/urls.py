from django.urls import path
from .views import say_hello, \
    get_pages_list, PostListView, \
    PostCreateView, PostDetailView, PostUpdateView, \
    PostDeleteView, PageCreateView, PageDetailView, \
    PageUpdateView, PageDeleteView


urlpatterns = [
    path('index/', say_hello),
    path('pages/', get_pages_list),
    path('posts/', PostListView.as_view()),
    path('post_create/', PostCreateView.as_view()),
    path('post/<int:pk>', PostDetailView.as_view()),
    path('post_update/<int:pk>', PostUpdateView.as_view()),
    path('post_delete/<int:pk>', PostDeleteView.as_view()),
    path('page_create/', PageCreateView.as_view()),
    path('page/<int:pk>', PageDetailView.as_view()),
    path('page_update/<int:pk>', PageUpdateView.as_view()),
    path('page_delete/<int:pk>', PageDeleteView.as_view())

]