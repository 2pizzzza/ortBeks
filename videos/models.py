from django.core.validators import FileExtensionValidator
from django.db import models

from courses.models import Course
from main.settings import TEST_VIDEO_FOLDER


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to=TEST_VIDEO_FOLDER, validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'video'
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f'Видео {self.title} по курсу {self.course.title}'
