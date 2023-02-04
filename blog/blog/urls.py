from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("news_feed/", include("news_feed.urls")),
    path("todo/", include("todo.urls"))

]
