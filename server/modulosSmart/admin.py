from django.contrib import admin
from .models import Usuario ,ModeloDisposivito,Tipo_user,Sala,Setor,Registro_Uso,Dispositivos,Comando,modulo_smart,RegistroLog

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id","login","nivel","nome","senha")

class TipoAdmin(admin.ModelAdmin):
    list_display = ("id","nome")

class SalaAdmin(admin.ModelAdmin):
    list_display = ("id","nome","local")
    
class Registro_UsoAdmin(admin.ModelAdmin):
    list_display = ("id","comeco","fim","sala")

class DispositivosAdmin(admin.ModelAdmin):
    list_display = ("id","modelo","sala","status")

class ModeloDisposivitoAdmin(admin.ModelAdmin):
    list_display = ("id","nome","marca","modelo")

class ComandoAdmin(admin.ModelAdmin):
    list_display = ("id","nome","codigo","modelo")

class RegistroLogAdmin(admin.ModelAdmin):
    list_display = ("id","dispositivo","comando","usuario","created_date")

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Tipo_user,TipoAdmin)
admin.site.register(Sala,SalaAdmin)
admin.site.register(Setor,TipoAdmin)
admin.site.register(Registro_Uso,Registro_UsoAdmin)
admin.site.register(Dispositivos,DispositivosAdmin)
admin.site.register(ModeloDisposivito,ModeloDisposivitoAdmin)
admin.site.register(Comando,ComandoAdmin)
admin.site.register(modulo_smart)
admin.site.register(RegistroLog,RegistroLogAdmin)



