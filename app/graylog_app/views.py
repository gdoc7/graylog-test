# from logging_config import gelf_logger  # Importa el logger configurado
#
#
# def mi_vista(request):
#     gelf_logger.error(
#         "Error con extras",
#         extra={
#             "user_id": 12345,
#             "ip": "192.168.1.100",
#             "service": "auth_api",
#         },
#     )
#     return HttpResponse("Log enviado a Graylog ")
# import logging
#
# logger = logging.getLogger(__name__)
#
#
# def mi_vista(request):
#     try:
#         logger.debug("Entrando en la vista")
#         # Tu código aquí...
#         logger.info(
#             "Operación exitosa",
#             extra={"user": request.user.username, "path": request.path},
#         )
#     except Exception as e:
#         logger.error(f"Error en la vista: {str(e)}", exc_info=True)
#         raise
from django.http import HttpResponseForbidden
import logging

logger = logging.getLogger()


def vista_error_500(request):
    logger.error("Error 403 actualizado", extra={"user_id": 12345})
    return HttpResponseForbidden("Acceso prohibido.")
