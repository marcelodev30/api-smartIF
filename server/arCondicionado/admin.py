from django.contrib import admin
from .models import Usuario,ServerMQTT,Sala,Modulo_IF_Smart,Dispositivos,Modelo_Dispositivos


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id","login","senha","nivel","img_url","nome") 

class ServerMQTTAdmin(admin.ModelAdmin):
    list_display = ("id","usuario","senha","host") 

class SalaAdmin(admin.ModelAdmin):
    list_display = ("id","nome","temperatura","dispositivo") 

class Modelo_DispositivosAdmin(admin.ModelAdmin):
    list_display = ("id","tipo","marca","modelo","codigo_IR") 

class Modulo_IF_SmartAdmin(admin.ModelAdmin):
    list_display = ("id","nome","temperatura","status","serverMQTT","Dispositivos") 

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(ServerMQTT,ServerMQTTAdmin)
admin.site.register(Modulo_IF_Smart)
admin.site.register(Modelo_Dispositivos,Modelo_DispositivosAdmin)
admin.site.register(Sala)
admin.site.register(Dispositivos)
