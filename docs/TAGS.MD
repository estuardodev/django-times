# Tags

## Etiqueta `day_now`

```python
{% day_now %}
{% day_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna el dia actual de acuerdo con la zona horaria configurada en las opciones (TIME_ZONE) de Django.
>
> Uso: Puedes usar {% day_now %} para obtener el dia actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% day_now 'America/Guatemala' %}.

------------

## Etiqueta `month_now`

```python
{% month_now %}
{% month_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna el mes actual.
>
> Uso: Puedes usar {% month_now %} para obtener el mes actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% month_now 'America/Guatemala' %}.

------------

## Etiqueta `year_now`

```python
{% year_now %}
{% year_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna el año actual.
>
> Uso: Puedes usar {% year_now %} para obtener el año actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% year_now 'America/Guatemala' %}.

------------

## Etiqueta `date`

```python
{% date %}
{% date 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna la fecha actual.
>
> Uso: Puedes usar {% date %} para obtener la fecha actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% date 'America/Guatemala' %}.

------------

## Etiqueta `hour_now`

```python
{% hour_now %}
{% hour_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
{% hour_now '' 12 %}  # Opcional: Puede especificar el formato de hora que deseas utilizar
```

> Descripcion: Retorna la hora actual.
>
> Uso: Puedes usar {% hour_now %} para obtener la hora actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% hour_now 'America/Guatemala' %}.

------------

## Etiqueta `minute_now`

```python
{% minute_now %}
{% minute_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna los minutos actuales.
>
> Uso: Puedes usar {% minute_now %} para obtener los minutos actuales. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% minute_now 'America/Guatemala' %}.

------------

## Etiqueta `second_now`

```python
{% second_now %}
{% second_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna los segundos actuales.
>
> Uso: Puedes usar {% second_now %} para obtener los segundos actuales. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% second_now 'America/Guatemala' %}.

------------

## Etiqueta `date_time_now`

```python
{% date_time_now %}
{% date_time_now 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
{% date_time_now '' 12 %}  # Opcional: Puede especificar el formato de hora que deseas utilizar
```

> Descripcion: Retorna la fecha y hora actual.
>
> Uso: Puedes usar {% date_time_now %} para obtener la fecha y hora actual. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% date_time_now 'America/Guatemala' %}.

------------

## Etiqueta `date_time_now_info`

```python
{% date_time_now_info %}
{% date_time_now_info 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
{% date_time_now_info 'America/Guatemala' 'es' %}  # Opcional: Puede especificar una zona horaria y un idioma personalizados
{% date_time_now_info '' '' 12 %}  # Opcional: Puede especificar el formato de hora que deseas utilizar
```

> Descripcion: Retorna la fecha y hora actual con informacion detallada.
>
> Uso: Puedes usar {% date_time_now_info %} para obtener la fecha y hora actual con informacion detallada. Tambien puedes especificar una zona horaria personalizada y un idioma personalizado, por ejemplo, {% date_time_now_info 'America/Guatemala' 'es' %}.

------------

## Etiqueta `date_time_now_rss`

```python
{% date_time_now_rss %}
{% date_time_now_rss 'America/Guatemala' %}  # Opcional: Puede especificar una zona horaria personalizada
```

> Descripcion: Retorna la fecha y hora actual en el formato estandar RSS.
>
> Uso: Puedes usar {% date_time_now_rss %} para obtener la fecha y hora actual en el formato RSS. Tambien puedes especificar una zona horaria personalizada, por ejemplo, {% date_time_now_rss 'America/Guatemala' %}.

------------

## Etiqueta `clock_update`

```python
{% clock_update %}
{% clock_update 12 %}  # Opcional: Puede especificar el formato de hora que deseas utilizar
```

> Descripcion: Retorna un reloj que se actualiza cada segundo.
>
> Uso: Puedes usar {% clock_update %} para agregar un reloj que se actualiza automaticamente cada segundo en tu pagina web.
