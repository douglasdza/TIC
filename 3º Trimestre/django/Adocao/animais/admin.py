from django.contrib import admin

# Importar os modelos
from .models import *

# Register your models here - Admin Django
admin.site.register(Cidade)
admin.site.register(Pessoa)
admin.site.register(Animal)
admin.site.register(Tipo)
