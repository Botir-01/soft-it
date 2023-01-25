from decouple import config

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['192.168.10.8', 'localhost', '127.0.0.1', 'api.softit.sport.uz']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config("NAME"),
        'USER': config("USER"),
        'PASSWORD': config('PASSWORD'),
        'HOST': config("HOST"),
        'PORT': config('PORT'),
    }
}
