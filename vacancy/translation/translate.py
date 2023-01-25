from modeltranslation.translator import TranslationOptions, register
from vacancy.models import Vacancy, VacanyRequirement, VacanyTask, VacanyCondition


@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = (
        'title', 'working_days', 
    )

@register(VacanyRequirement)
class VacanyRequirementTranslationOptions(TranslationOptions):
    fields = (
        'content', 
    )

@register(VacanyTask)
class VacanyTaskTranslationOptions(TranslationOptions):
    fields = (
        'content', 
    )

@register(VacanyCondition)
class VacanyConditionTranslationOptions(TranslationOptions):
    fields = (
        'content', 
    )
