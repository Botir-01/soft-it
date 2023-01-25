from django.contrib import admin
from .models import Menu, CompanyInfo, AboutCompany, CompanyImage
# Register your models here.
admin.site.register(Menu)
admin.site.register(CompanyInfo)

class CompanyImageInline(admin.TabularInline):
    model = CompanyImage

class AboutCompanyAdmin(admin.ModelAdmin):
    inlines = (CompanyImageInline, )

admin.site.register(AboutCompany, AboutCompanyAdmin)