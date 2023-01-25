from decouple import config
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'softit',
        'USER': 'root',
        'PASSWORD': 'Bo977731030#',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
