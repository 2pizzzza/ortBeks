from rest_framework import generics, permissions
from . import models as m, serializers as s


class NewsCreateAPIView(generics.CreateAPIView):
    serializer_class = s.NewsSerializer
    permission_classes = [permissions.IsAdminUser]


class NewsListAPIView(generics.ListAPIView):
    queryset = m.News.objects.all()
    serializer_class = s.NewsSerializer


class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.News.objects.all()
    serializer_class = s.NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
