# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '==wwsyb)h^*v(s=m$2o2uq*8u(dfu(&q*oj#^2@)a2-pse2idn'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stacked',
        'USER': 'davidmohrmann',
        'PASSWORD': 'admin123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
