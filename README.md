# Travel Blog Project

Travel blog project es una aplicación web desarrollada utilizando Django y Python. Es una plataforma que te permite descubrir, crear y compartir blogs fascinantes sobre viajes.

## Cómo Probar

1. Clona este repositorio.
2. Crea un entorno virtual: `python -m venv venv`.
3. Activa el entorno virtual: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows).
4. Instala las dependencias: `pip install -r requirements.txt`.
5. Realiza las migraciones: `python manage.py migrate`.
6. Crea un superusuario: `python manage.py createsuperuser`.
7. Inicia el servidor: `python manage.py runserver`.

## Funcionalidades

1. Registro y Autenticación:

- URL: /
- Los usuarios deben registrarse para poder navegar por la plataforma. Una vez registrado, podrás iniciar sesión con tus credenciales.

2. Edición de Perfil:

- URL: /pages/update_profile
- Los usuarios pueden actualizar su información de perfil, incluyendo su nombre de usuario, contraseña y dirección de correo electrónico.

3. Página Principal

- URL: /pages
- Muestra una lista de todos los posts disponibles.

4. Crear un Nuevo Post

- URL: /page/create
- Descripción: Permite a los usuarios crear un nuevo post ingresando título, subtitilo y descripcion y subir una foto.
