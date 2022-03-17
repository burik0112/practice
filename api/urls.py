from django.urls import path

from api.views import CategoryListAPIView, ContactListAPIView, PostListCreateAPIView

app_name = 'swagger'


urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('posts/', PostListCreateAPIView.as_view()),
    path('contact/', ContactListAPIView.as_view())

]