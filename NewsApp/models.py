from django.db import models
from django.utils import timezone


# Create your models here.
class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='news',
    )

    def get_absolute_url(self):
        return '/news/{0}'.format(self.pk)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Комментарии к новости
    """
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    news = models.ForeignKey('News')

    def __str__(self):
        return self.text
