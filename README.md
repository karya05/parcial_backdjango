
# Peticiones HTTP en Django

En este proyecto se creó un endpoint usando Django nativo, sin instalar librerías externas. La vista `ProjectEndpoint` trabaja con los proyectos guardados en la base de datos y utiliza los cuatro métodos HTTP.

GET permite consultar los proyectos (Read), POST permite crear un proyecto (Create), PUT permite actualizarlo (Update) y DELETE permite eliminarlo (Delete). Estas operaciones corresponden al modelo CRUD.

Para desarrollar el endpoint se utilizaron los siguientes elementos:

- `View`: permite crear una vista basada en clase.
- `JsonResponse`: devuelve respuestas en formato JSON.
- `json.loads()`: lee los datos enviados en formato JSON.
- `parse_date()`: convierte una fecha de texto en una fecha válida.
- `path()`: define las rutas de la aplicación.
- `include()`: conecta las rutas de la aplicación con el proyecto principal.
- `as_view()`: permite utilizar la vista basada en clase en las rutas.
- `csrf_exempt`: excluye la vista de la protección CSRF.
- `method_decorator`: permite aplicar el decorador a la clase.
- `Project.objects.get()`: busca un proyecto en la base de datos.
- `Project.objects.create()`: crea un proyecto nuevo.
- `save()`: guarda los cambios realizados.
- `delete()`: elimina un proyecto.

El desarrollo se encuentra en `gestion/views.py`, las rutas de la aplicación están en `gestion/urls.py` y la conexión con el proyecto principal se encuentra en `backend/urls.py`.

**Fuentes consultadas**

- Vistas basadas en clase: https://docs.djangoproject.com/en/6.1/topics/class-based-views/
- Solicitudes y respuestas HTTP: https://docs.djangoproject.com/en/6.1/ref/request-response/
- Protección CSRF: https://docs.djangoproject.com/en/6.1/ref/csrf/