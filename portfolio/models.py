from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Project(models.Model):
    title = models.CharField(max_length=500)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/project')
    is_main = models.BooleanField(default=False)
    project_category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'