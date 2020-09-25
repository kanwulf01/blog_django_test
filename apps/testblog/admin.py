from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CategoriaResource(resources.ModelResource):

    class Meta:
        model = Categoria



class AuthorResource(resources.ModelResource):

    class Meta:
        model = Autor


class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion')
    resource_class = CategoriaResource

class AuthorAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('nombres','apellidos','facebook','twitter','instagram', 'web','correo','estado','fecha_creacion',)
    resource_class = AuthorResource
    

#register recive 2 parametros nombre del modelo y una clase que herede de categoriaadmin para visualizar instancias del modelo
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AuthorAdmin)