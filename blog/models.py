from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    slug = models.CharField(max_length=300, **NULLABLE, verbose_name='slug')
    content = models.TextField(verbose_name='content')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='preview')
    date_created = models.DateField(verbose_name='date_created')
    view_count = models.IntegerField(default=0, verbose_name='view_count')
    is_published = models.BooleanField(default=True, verbose_name='is_published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'