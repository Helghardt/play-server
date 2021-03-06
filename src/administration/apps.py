# LOGGING
# ---------------------------------------------------------------------------------------------------------------------#
import logging
logger = logging.getLogger('django')


# IMPORTS
# ---------------------------------------------------------------------------------------------------------------------#
from django.apps import AppConfig


# APP CONFIG
# ---------------------------------------------------------------------------------------------------------------------#
class CustomConfig(AppConfig):
    name = 'administration'
    verbose_name = 'Administration'