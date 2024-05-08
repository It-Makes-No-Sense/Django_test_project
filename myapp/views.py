from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed.')
    return HttpResponse("Hello, world.")


def about(request):
    try:
        result = 1/0
    except Exception as e:
        logger.exception(f'Error in about page. {e}')
        return HttpResponse("Oops! Something went wrong.")
    else:
        logger.info('About page accessed.')
        return HttpResponse("This is the about page.")

