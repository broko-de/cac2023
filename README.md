# Proyecto Django Codo A Codo (CAC)- 2023

Este es un proyecto de software desarrollado en python 🐍 por medio del framework Django 🦄.  Con el se busca implementar los contenidos vistos durante la cursada abarcando temas como:

- Creación y configuración de proyecto Django;
- Aplicaciones;
- Patron MVT - (Modelo-Vista-Template);
- Manejo de archivos estáticos y media;
- Panel Admin de Django;
- Autenticación y autorización;
- Django RestFramework;
- Base de datos (PostgreSQL)

### Instalacion
Hay que tener en cuenta que se necesita un motor de base de datos relacional, puede ser PostgreSQL (recomendado) o Mysql. Para poder correr el proyecto, vas a tener que seguir los siguientes pasos (para sistema operativo Windows):

1. Clonar el repositorio del repositorio
```
git clone https://github.com/broko-de/cac2023.git
cd cac2023
```
2. Crear un entorno virtual para el proyecto y activarlo
```
python -m venv env
env/bin/activate
```
3. Instalar las dependencias del proyecto
```
pip install -r requirements.txt
```
4. Crear un archivo .env en el directorio cac2023 a la misma altura del archivo settings.py y completar con los datos de configuración segun lo indica .env.example
5. Correr las migraciones del proyecto
```
python manage.py migrate
```
6. Por último, correr el servidor de desarrollo que provee Django
```
python manage.py runserver
```
