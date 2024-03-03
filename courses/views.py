from rest_framework import generics, permissions

from . import models as m, serializers as s


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = s.CourseSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseListAPIView(generics.ListAPIView):
    queryset = m.Course.objects.all()
    serializer_class = s.CourseSerializer


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Course.objects.all()
    serializer_class = s.CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
