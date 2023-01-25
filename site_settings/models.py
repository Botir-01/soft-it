from django.db import models
from django.conf import settings

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500, null=True)
    order = models.IntegerField()
    is_footer = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='childs', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        db_table = 'menu'
        ordering = ['order']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'   


class CompanyInfo(models.Model):
    logo_title = models.CharField(max_length=100)
    logo_description = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    
    telegram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    email = models.EmailField()
    logo = models.FileField(upload_to='company/logo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def logo_url(self):
        if self.logo:
            return "%s%s" % (settings.HOST, self.logo.url)
        
    def __str__(self):
        return self.logo_title


    class Meta:
        db_table = 'company_info'
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'


class AboutCompany(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'about_company'
        verbose_name = 'O компании'
        verbose_name_plural = 'O компании'


class CompanyImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='company/image')
    is_main = models.BooleanField(default=False)
    company_id = models.ForeignKey(AboutCompany, on_delete=models.CASCADE, related_name='photos')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_id.title 

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)
        
    class Meta:
        db_table = 'company_image'
        verbose_name = 'Фотография компании'
        verbose_name_plural = 'Фотографии компании'