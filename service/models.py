from django.db import models
from django.conf import settings

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_main = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'service'
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class Partner(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    link = models.URLField(blank=True, null=True)
    image = models.FileField(upload_to='partner/images')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'partner'
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'