from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail

@csrf_exempt
def notifier(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            evento = data.get('evento')
            usuario = data.get('usuario')

            # Ejemplo de mensaje
            mensaje = f"Nuevo evento: {evento}\nUsuario: {usuario['nombre']} - {usuario['email']}"

            # Enviar correo
            send_mail(
                subject=f"Notificación: {evento}",
                message=mensaje,
                from_email='tu_email@gmail.com',
                recipient_list=['admin@tuapp.com'],
                fail_silently=False,
            )

            return JsonResponse({'mensaje': 'Notificación enviada correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
