from modeltranslation.translator import TranslationOptions, register
from blog.models import BlogCategory, Blog


@register(BlogCategory)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = (
        'title', 
    )

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = (
        'title', 'short_description', 'description', 
    )