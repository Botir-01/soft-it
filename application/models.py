from django.db import models
from portfolio.models import Category

# Create your models here.
class CustomerApplication(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return "From " + self.full_name

    class Meta:
        db_table = 'customer_application'
        verbose_name = 'Проект клиента'
        verbose_name_plural = 'Проекты клиента'


class CustomerProjectApplication(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100)
    project_category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='customer_projects')
    description = models.TextField()

    
    def __str__(self):
        if self.company_name:
            return self.company_name
        else:
            return self.full_name

    class Meta:
        db_table = 'customer_project_application'
        verbose_name = 'Проект клиента в делатях'
        verbose_name_plural = 'Проекты клиента в делатях'
