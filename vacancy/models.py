from django.db import models

# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    working_days = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=100)
    is_main = models.BooleanField(default=False)
    salary = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'vacancy'
        verbose_name = 'Ваканcия'
        verbose_name_plural = 'Ваканcии'


class VacanyRequirement(models.Model):
    content = models.CharField(max_length=255)
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='requirements')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'vacancy_requirements'
        verbose_name = 'Требование ваканcии'
        verbose_name_plural = 'Требования ваканcии'


class VacanyTask(models.Model):
    content = models.CharField(max_length=255)
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='tasks')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'vacancy_tasks'
        verbose_name = 'Задача ваканции'
        verbose_name_plural = 'Задачи ваканции'


class VacanyCondition(models.Model):
    content = models.CharField(max_length=255)
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='conditions')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'vacancy_conditions'
        verbose_name = 'Условие ваканcии'
        verbose_name_plural = 'Условия ваканcии'


class UserResume(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='resumes')
    cv_file = models.FileField(upload_to='resumes/file')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From " + self.full_name

    class Meta:
        db_table = 'resume'
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'