from modeltranslation.translator import TranslationOptions, register
from site_settings.models import Menu, CompanyInfo, AboutCompany, CompanyImage


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = (
        'title', 
    )


@register(CompanyInfo)
class CompanyInfoTranslationOptions(TranslationOptions):
    fields = (
        'logo_description', 
    )


@register(AboutCompany)
class AboutCompanyTranslationOptions(TranslationOptions):
    fields = (
        'title', 'short_description', 'description',
    )


@register(CompanyImage)
class CompanyImageTranslationOptions(TranslationOptions):
    fields = (
        'title', 'content',
    )