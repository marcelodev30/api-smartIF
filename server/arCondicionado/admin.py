from django.contrib import admin
from models import Usuario,ServerMQTT,Dispositivos,Sala


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id","login","senha","nivel","img_url","nome") 

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(ServerMQTT)
admin.site.register(Dispositivos)
admin.site.register(Sala)
