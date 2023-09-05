from django.conf import settings
from babel import Locale, dates
import pytz
from datetime import datetime

# Here utilities to improve the system
try:
    timezone_settings = settings.TIME_ZONE
    language_settings = settings.LANGUAGE_CODE
except:
    timezone_settings = "UTC"
    language_settings = 'en-us'

def get_timezone(timezone_name):
    try:
        user_timezone = pytz.timezone(timezone_name)
    except pytz.UnknownTimeZoneError:
        user_timezone = pytz.utc 
    return user_timezone

def get_formatted_time(timezone_name, format_string):
    """
    Obtiene la hora actual formateada según la zona horaria y el formato especificados.

    Args:
        timezone_name (str): El nombre de la zona horaria para la que se formateará la hora.
        format_string (str): El formato en el que se desea formatear la hora.

    Returns:
        str: La hora actual formateada según el formato especificado.
    """
    user_timezone = get_timezone(timezone_name)
    current_time = datetime.now(user_timezone)
    formatted_time = current_time.strftime(format_string)
    return str(formatted_time)

def get_formatted_time_traslate(timezone_name, format_string, language):
    """
    Obtiene una zona horaria a partir de su nombre.

    Args:
        timezone_name (str): El nombre de la zona horaria a obtener.
        format_string (str): Formato que se solicita.
        language (str): Idioma el cual desea la hora

    Returns:
        timezone: La zona horaria correspondiente al nombre proporcionado.
    """

    user_timezone = get_timezone(timezone_name)
    current_time = datetime.now(user_timezone)

    language_parts = language.split('-')
    language_code = language_parts[0]

    locale = Locale(language_code)

    formatted_time = None
    
    if format_string == "%d":
        formatted_time = dates.format_date(current_time, format='d', locale=locale)
    elif format_string == "%m":
        formatted_time = dates.format_date(current_time, format='M', locale=locale)
    elif format_string == "%Y":
        formatted_time = dates.format_date(current_time, format='y', locale=locale)
    elif format_string == "%d/%m/%Y":
        formatted_time = dates.format_date(current_time, format='short', locale=locale)
    elif format_string == "%H":
        formatted_time = dates.format_time(current_time, format='H', locale=locale)
    elif format_string == "%M":
        formatted_time = dates.format_time(current_time, format='m', locale=locale)
    elif format_string == "%S":
        formatted_time = dates.format_time(current_time, format='s', locale=locale)
    elif format_string == "%Y-%m-%dT%H:%M:%S":
        formatted_time = dates.format_datetime(current_time, format='iso', locale=locale)
    elif format_string == "%A, %d. %B %Y %I:%M%p":
        formatted_time = dates.format_datetime(current_time, format='full', locale=locale)
    
    return formatted_time
