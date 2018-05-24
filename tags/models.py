from django.db import models


class Tag(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    tag = models.CharField(max_length=50, verbose_name='Тег', unique=True)

    def __str__(self):
        return self.tag

    def as_dict(self):
        return {'id': self.id, 'tag': self.tag}
