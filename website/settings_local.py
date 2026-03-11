# website/settings_local.py
import os
from .settings import BASE_DIR

# Используем SQLite для разработки
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Или если хотите использовать PostgreSQL:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'netology_orm_migrations',
#         'USER': 'postgres',  # замените на вашего пользователя
#         'PASSWORD': 'postgres',  # замените на ваш пароль
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DEBUG = True