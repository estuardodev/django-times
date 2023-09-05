# Django Times

Django Times es un modulo el cual busca mejorar y optimizar el trabajo al momento de pasar fechas y dias a los templates en django y asi mejorar el mantenimiento del codigo.

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-0.0.1-gree)](CHANGELOG.md)
[![Contributors](https://img.shields.io/github/contributors/estuardodev/django-times)](https://github.com/estuardodev/django-times/graphs/contributors)

</div>

## Informacion General

Este proyecto proporciona una biblioteca que facilita el trabajo con fechas y horas en aplicaciones Django. Ofrece una serie de etiquetas y funciones personalizadas que permiten obtener y formatear la fecha y hora actual, asi como configurar la zona horaria y el idioma en algunos casos.

## Proyecto

Este proyecto tiene como objetivo simplificar el manejo de fechas y horas en aplicaciones Django. Algunos de los aspectos clave del proyecto incluyen:

- Obtener la fecha y hora actual de acuerdo con la zona horaria configurada en las opciones de Django.
- Formatear la fecha y hora de diferentes maneras segun las necesidades del usuario.
- Personalizar la zona horaria y el idioma para adaptarse a requisitos especificos.

## Instrucciones de Uso

### Instalacion

Para utilizar esta biblioteca en tu proyecto Django, sigue estos pasos:

1. Crea un entorno virtual para tu proyecto (se recomienda, pero opcional).

    ```
    py -m venv env # Windows
    python3 -m virtualenv env # Linux
    ```

2. Activa el entorno virtual

    ```
	.\env\Scripts\activate # Windows
	source env/bin/activate # Linux
    ```

3. Instala los django_times

    `pip install django-times`

4. INSTALLED_APPS
    ```
	INSTALLED_APPS = [
	...
	'django_times',
	...
    ]
    ```

5. Recoger archivos estaticos

    ```
	py manage.py collectstatic # Windows
	python3 manage.py collectstatic # Linux
    ```

### Uso
Para usar django times dentro de tus plantillas de django debes de cargar el tag, para ello usa:

	{% load django_times %}

Y ya puedes usar los distintos tags que te ofrece django-times:
#### Tags
##### Etiqueta `day_now`

```python
{% day_now %}
{% day_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna el dia actual de acuerdo con la zona horaria configurada en las opciones (TIME_ZONE) de Django.

> Uso: Puedes usar {% day_now %} para obtener el dia actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% day_now 'America/Guatemala' %}.


------------


##### Etiqueta `month_now`

```python
{% month_now %}
{% month_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna el mes actual.

> Uso: Puedes usar {% month_now %} para obtener el mes actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% month_now 'America/Guatemala' %}.

------------

##### Etiqueta `year_now`

```python
{% year_now %}
{% year_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna el año actual.

> Uso: Puedes usar {% year_now %} para obtener el año actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% year_now 'America/Guatemala' %}.

------------

##### Etiqueta `date`

```python
{% date %}
{% date 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna la fecha actual.

> Uso: Puedes usar {% date %} para obtener la fecha actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% date 'America/Guatemala' %}.

------------

##### Etiqueta `hour_now`

```python
{% hour_now %}
{% hour_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna la hora actual.

> Uso: Puedes usar {% hour_now %} para obtener la hora actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% hour_now 'America/Guatemala' %}.

------------

##### Etiqueta `minute_now`

```python
{% minute_now %}
{% minute_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna los minutos actuales.

> Uso: Puedes usar {% minute_now %} para obtener los minutos actuales. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% minute_now 'America/Guatemala' %}.

------------

##### Etiqueta `second_now`

```python
{% second_now %}
{% second_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna los segundos actuales.

> Uso: Puedes usar {% second_now %} para obtener los segundos actuales. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% second_now 'America/Guatemala' %}.

------------

##### Etiqueta `date_time_now`

```python
{% date_time_now %}
{% date_time_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna la fecha y hora actual.

> Uso: Puedes usar {% date_time_now %} para obtener la fecha y hora actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% date_time_now 'America/Guatemala' %}.

------------

##### Etiqueta `date_time_now_info`

```python
{% date_time_now_info %}
{% date_time_now_info 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
{% date_time_now_info 'America/Guatemala' 'es' %}  # Opcional: Puede especificar una zona horaria y un idioma personalizados
```

> Descripcion: Retorna la fecha y hora actual con informacion detallada.

> Uso: Puedes usar {% date_time_now_info %} para obtener la fecha y hora actual con informacion detallada. Tambien puedes especificar una zona horaria personalizada y un idioma personalizado, por ejemplo, {% date_time_now_info 'America/Guatemala' 'es' %}.

------------

##### Etiqueta `date_time_now_rss`

```python
{% date_time_now_rss %}
{% date_time_now_rss 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna la fecha y hora actual en el formato estandar RSS.

> Uso: Puedes usar {% date_time_now_rss %} para obtener la fecha y hora actual en el formato RSS. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% date_time_now_rss 'America/Guatemala' %}.

------------

##### Etiqueta `clock_update`

```python
{% clock_update %}
```

> Descripcion: Retorna un reloj que se actualiza cada segundo.

> Uso: Puedes usar {% clock_update %} para agregar un reloj que se actualiza automaticamente cada segundo en tu pagina web.

## Contribucion
¡Gracias por considerar contribuir a este proyecto! Si deseas contribuir, sigue estos pasos:

1. Crea un fork del repositorio en GitHub.

2. Clona tu repositorio fork en tu entorno de desarrollo local.
`git clone https://github.com/TU_NOMBRE_DE_USUARIO/django-times.git`

3. Crea una rama para tu contribucion.
`git checkout -b mi-contribucion`

4. Realiza tus cambios y realiza confirmaciones significativas.

5. Envia una solicitud de extraccion (pull request) a la rama principal del proyecto.

6. Tu solicitud de extraccion sera revisada y, si es aceptada, se fusionara con el proyecto principal.

> Recuerda siempre editar el archivo CHANGELOG.md indicando que cambios realizastes, tambien se descriptivo en el mensaje de tu commit y  agrega tu nombre a CONTRIBUTORS siguiendo el orden alfabetico.
