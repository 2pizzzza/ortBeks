from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'course'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'Курс {self.title}'
