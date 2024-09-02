from django.contrib import admin
from .models import Usuario,ServerMQTT,Dispositivos,Sala


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id","login","senha","nivel","img_url","nome") 

class ServerMQTTAdmin(admin.ModelAdmin):
    list_display = ("id","usuario","senha","host") 

class SalaAdmin(admin.ModelAdmin):
    list_display = ("id","nome","temperatura","dispositivo") 

class DispositivosAdmin(admin.ModelAdmin):
    list_display = ("id","nome","temperatura","status","serverMQTT") 

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(ServerMQTT,ServerMQTTAdmin)
admin.site.register(Dispositivos,DispositivosAdmin)
admin.site.register(Sala,SalaAdmin)
