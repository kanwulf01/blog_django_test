from django.contrib import admin
from .models import *
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):

    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion')

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('nombres','apellidos','facebook','twitter','instagram', 'web','correo','estado','fecha_creacion',)
    

#register recive 2 parametros nombre del modelo y una clase que herede de categoriaadmin para visualizar instancias del modelo
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AuthorAdmin)