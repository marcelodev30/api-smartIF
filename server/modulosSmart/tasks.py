from celery import shared_task
from django.utils import timezone
from .models import Registro_Cenários
from .send_mqtt import send_mqtt

@shared_task
def verificar_e_executar_cenarios():
    agora = timezone.now()
    cenarios = Registro_Cenários.objects.filter(status=True, data__lte=agora)
    for cenario in cenarios:
        send_mqtt(cenario.dispositivo.id,cenario.ação)
        cenario.status = False  # Desativa o cenário após a execução
        cenario.save()
        print(f"Executando cenário")

 

   