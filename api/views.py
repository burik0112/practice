from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView

from api.serializers import CategorySerializer, PostSerializer, ContactSerializer
from posts.models import CategoryModel, PostModel


class CategoryListAPIView(ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()


class PostListCreateAPIView(ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()


class ContactListAPIView(ListAPIView):
    serializer_class = ContactSerializer
    queryset = PostModel.objects.all()
