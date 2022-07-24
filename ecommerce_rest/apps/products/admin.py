from django.contrib import admin
from apps.products.models import *

# Register your models here.


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id','description')

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id','description')
    # OPCIONES DE CONFIGURACIÓN DEL ADMIN
    # ordering = ('creditos', 'nombre')
    # search_fields = ('nombre', 'creditos')
    # list_editable = ('nombre', 'creditos')
    # list_display_links = ('nombre',)
    # list_filter= ('creditos',) 
    # list_per_page= 3 # Paginación
    # exclude= ('creditos',)

    # Permite que no se puedan eliminar las categorias desde el Admin.
    def get_actions (self,request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions


admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicador)
admin.site.register(Product)

