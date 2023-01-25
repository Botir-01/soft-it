from django.urls import path, include
from rest_framework.routers import DefaultRouter
from site_settings.views import HeaderView, IndexView, FooterView, AboutView
from application.views import CustomerApplicationView, CustomerProjectApplicationView
from service.views import ServiceView
from portfolio.views import CategoryView, ProjectView
from vacancy.views import VacancyView, UserResumeView
from blog.views import BlogCategoryView, BlogView

router = DefaultRouter()
router.register(r'header', HeaderView, basename='header')
router.register(r'index', IndexView, basename='index')
router.register(r'footer', FooterView, basename='footer')
router.register(r'about', AboutView, basename='about')
router.register(r'applications', CustomerApplicationView, basename='customer_application')
router.register(r'project-applications', CustomerProjectApplicationView, basename='customer_application')
router.register(r'services', ServiceView, basename='service')
router.register(r'project-categories', CategoryView, basename='project-category')
router.register(r'projects', ProjectView, basename='project')
router.register(r'vacancies', VacancyView, basename='vacancy')
router.register(r'resumes', UserResumeView, basename='resume')
router.register(r'blog-categories', BlogCategoryView, basename='blog-category')
router.register(r'blogs', BlogView, basename='blogs')

urlpatterns = [
    path(r'', include(router.urls))               
]