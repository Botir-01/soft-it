from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

COVER = [200, 200]
BANNER = [1300, 500]


# Create your models here.
class BlogCategory(models.Model):
    title = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_category'
        verbose_name = 'Категория блогов'
        verbose_name_plural = 'Категории блогов'


class Blog(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    views = models.IntegerField(default=0)
    published_date = models.DateField()
    blog_category_id = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs')
    cover_image = ResizedImageField(upload_to='blog/', size=COVER, blank=True, null=True)
    banner_image = ResizedImageField(upload_to='blog/', size=BANNER, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def cover_image_url(self):
        if self.cover_image:
            return "%s%s" % (settings.HOST, self.cover_image.url)

    @property
    def banner_image_url(self):
        if self.banner_image:
            return "%s%s" % (settings.HOST, self.banner_image.url)

    
    def __str__(self):
        return self.title


    class Meta:
        db_table = 'blog'
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

