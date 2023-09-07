# Django Times

Django Times es un modulo el cual busca mejorar y optimizar el trabajo al momento de pasar fechas y dias a los templates en django y asi mejorar el mantenimiento del codigo.

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-0.1.1-gree)](CHANGELOG.md)
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

    ```python
    py -m venv env # Windows
    python3 -m virtualenv env # Linux
    ```

2. Activa el entorno virtual

    ```python
    .\env\Scripts\activate # Windows
    source env/bin/activate # Linux
    ```

3. Instala los django_times

    `pip install django-times`

4. INSTALLED_APPS

    ```python
    INSTALLED_APPS = [
        ...
        'django_times',
        ...
    ]
    ```

5. Recoger archivos estaticos

    ```python
    py manage.py collectstatic # Windows
    python3 manage.py collectstatic # Linux
    ```

### Uso

Para usar django times dentro de tus plantillas de django debes de cargar el tag, para ello usa:

 `{% load django_times %}`

Y ya puedes usar los distintos tags que te ofrece django-times:
[ver mas...](./docs/TAGS.MD)

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
