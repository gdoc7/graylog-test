from django.http import HttpResponseForbidden
import logging
import os

logger = logging.getLogger()


def vista_error_500(request):
    logger.info("SECRET", os.environ["SECRET"])
    return HttpResponseForbidden("Acceso prohibido")
