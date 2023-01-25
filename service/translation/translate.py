from modeltranslation.translator import TranslationOptions, register
from service.models import Service, Partner

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = (
        'title', 'description', 
    )

@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = (
        'title', 
    )