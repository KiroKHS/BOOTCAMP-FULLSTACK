# Taller de fullstack

se creara una pagina de venta de intrumentos musicales

inspiracion de [casa amarilla](https://www.casamarilla.cl/)

# se implemento django

## migration
1. `python manage.py makemigrations`
2. `python manage.py migrate`

## crear super usuario
`python manage.py createsuperuser` 

## poner español

line **107** a **setting.py** colocar **es**

## importacion nesesaria
 `sh
 pip install django-crispy-forms
 pip install pillow
 pip install djangorestframework
 `

# para instalar en oracle

`pip install cx_oracle`

## primer paso
creas un usuario y una base de datos

## ejemplo 
`
'default': {
        'ENGINE': 'django.db.backends.oracle',
        'host': 'localhost',
        'NAME': 'xe',
        'USER': 'django',
        'PASSWORD': 'django',
        'PORT': '1521',
    }
`

# datos de moledos

al generar un modelo sin una clave prymary key se crea una primary key id