# Imports
from django import template
from django.utils.safestring import mark_safe
from django_times.utils import get_formatted_time, get_formatted_time_traslate
from django_times.utils import timezone_settings, language_settings

register = template.Library()

# Etiquetas personalizadas

@register.simple_tag
def day_now(timezone_name=timezone_settings):
    '''
    Retorna el día actual de acuerdo con la zona horaria configurada en las opciones (TIME_ZONE).

    USO:

    {% day_now %}
    {% day_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    '''
    return get_formatted_time(timezone_name, "%d")

@register.simple_tag
def month_now(timezone_name=timezone_settings):
    '''
    Retorna el mes actual.

    USO:

    {% month_now %}
    {% month_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    '''
    return get_formatted_time(timezone_name, "%m")

@register.simple_tag
def year_now(timezone_name=timezone_settings):
    '''
    Retorna el año actual.

    USO:

    {% year_now %}
    {% year_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    '''
    return get_formatted_time(timezone_name, "%Y")

@register.simple_tag
def date(timezone_name=timezone_settings):
    '''
    Retorna la fecha actual.

    USO:

    {% date %}
    {% date 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    '''
    return get_formatted_time(timezone_name, "%d/%m/%Y")

@register.simple_tag
def hour_now(timezone_name=timezone_settings):
    '''
    Retorna la hora actual.

    USO:

    {% hour_now %}
    {% hour_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    '''
    return get_formatted_time(timezone_name, "%H")

@register.simple_tag
def minute_now(timezone_name=timezone_settings):
    '''
    Retorna los minutos actuales.

    USO:

    {% minute_now %}
    {% minute_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    '''
    return get_formatted_time(timezone_name, "%M")

@register.simple_tag
def second_now(timezone_name=timezone_settings):
    '''
    Retorna los segundos actuales.

    USO:

    {% second_now %}
    {% second_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    '''
    return get_formatted_time(timezone_name, "%S")

@register.simple_tag
def date_time_now(timezone_name=timezone_settings):
    '''
    Retorna la fecha y hora actual.

    USO:

    {% date_time_now %}
    {% date_time_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    '''
    return get_formatted_time(timezone_name, "%Y-%m-%dT%H:%M:%S")

@register.simple_tag
def date_time_now_info(timezone_name=timezone_settings, language=language_settings):
    '''
    Retorna la fecha y hora actual con información detallada.

    USO:

    {% date_time_now_info %}
    {% date_time_now_info 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    {% date_time_now_info 'America/Guatemala' 'es' %}  # Opcional: Puede especificar una zona horaria y un idioma personalizados
    '''
    return get_formatted_time_traslate(timezone_name, "%A, %d. %B %Y %I:%M%p", language)

@register.simple_tag
def date_time_now_rss(timezone_name=timezone_settings):
    '''
    Retorna la fecha y hora actual en el formato estándar RSS.

    USO:

    {% date_time_now_rss %}
    {% date_time_now_rss 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
    '''
    return get_formatted_time(timezone_name, '%a, %d %b %Y %H:%M:%S %z')

@register.simple_tag
def clock_update():
    '''
    Retorna un reloj que se actualiza cada segundo.

    USO:

    {% clock_update %}
    '''
    return mark_safe('<span id="currentDate"></span>\n<script src="static/django_times/clock.js" type="text/javascript"></script>')
