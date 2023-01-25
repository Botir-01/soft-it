from django.contrib import admin
from .models import Vacancy, VacanyRequirement, VacanyTask, VacanyCondition, UserResume
# Register your models here.

class VacanyRequirementInline(admin.TabularInline):
    model = VacanyRequirement

class VacanyTaskInline(admin.TabularInline):
    model = VacanyTask

class VacancyConditionInline(admin.TabularInline):
    model = VacanyCondition


class VacancyAdmin(admin.ModelAdmin):
    inlines = (VacanyRequirementInline, VacanyTaskInline, VacancyConditionInline, )


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(UserResume)