from modeltranslation.translator import TranslationOptions, register
from portfolio.models import Category, Project

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'title', 
    )

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = (
        'title', 
    )