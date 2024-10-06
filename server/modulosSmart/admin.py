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

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Tipo_user,TipoAdmin)
admin.site.register(Sala,SalaAdmin)
admin.site.register(Setor,TipoAdmin)
admin.site.register(Registro_Uso,Registro_UsoAdmin)
admin.site.register(Tipo,TipoAdmin)
admin.site.register(Dispositivos,DispositivosAdmin)
admin.site.register(Comando,ComandoAdmin)
admin.site.register(modulo_smart)



