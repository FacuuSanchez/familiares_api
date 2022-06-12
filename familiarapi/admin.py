from django.contrib import admin
from .models import Persona, Familiar

# Register your models here.
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('persona', 'documento', 'fecha_nacimiento')
    list_filter = ('persona', 'documento')
    search_fields = ('persona', 'documento')

@admin.register(Familiar)
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('persona', 'tipo_vinculo')
    list_filter = ('persona', 'tipo_vinculo')
    search_fields = ('persona', 'tipo_vinculo')