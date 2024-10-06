from django.contrib import admin
from .models import Usuario ,Tipo_user,Sala,Setor,Registro_Uso,Tipo,Dispositivos,Comando,modulo_smart

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id","login","senha","nivel","nome")

class TipoAdmin(admin.ModelAdmin):
    list_display = ("id","nome")
class SalaAdmin(admin.ModelAdmin):
    list_display = ("id","nome","local")
    
class Registro_UsoAdmin(admin.ModelAdmin):
    list_display = ("id","comeco","fim","sala")

class DispositivosAdmin(admin.ModelAdmin):
    list_display = ("id","tipo_id","marca","modelo","status","sala")

class ComandoAdmin(admin.ModelAdmin):
    list_display = ("id","nome","codigo","dispositivo")

admin.register(Usuario)
admin.register(Tipo_user)
admin.register(Sala)
admin.register(Setor)
admin.register(Registro_Uso)
admin.register(Tipo,TipoAdmin)
admin.register(Dispositivos)
admin.register(Comando)
admin.register(modulo_smart)



