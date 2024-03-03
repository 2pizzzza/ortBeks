from rest_framework import serializers
from . import models as m


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Video
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course_name'] = instance.course.title
        return representation
