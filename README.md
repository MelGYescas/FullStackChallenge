# DirectorioBack

Este proyecto fue generado con Django  y Django Rest Framework  para el reto Full Stack Challenge (Back-end).

## Descripción del reto

El reto consistía en procesar un archivo CSV que contenía información de una guía telefónica y representarla en una página web. Los datos del archivo CSV estaban desordenados y podían contener duplicados. La solución debía permitir al usuario cargar un archivo CSV, procesar los datos en el backend y presentar los resultados en el frontend.

## Solución

Para resolver el reto se utilizó Django y Django Rest Framework para el backend y Angular para el frontend. La aplicación consta de dos partes principales: una API que permite cargar y procesar el archivo CSV, y otra que muestra una tabla con los contactos. Los campos repetidos se marcan como tal en la base de datos y los campos inválidos se gestionan adecuadamente.
### Notas adicionales

Se eligieron Angular y Django como herramientas para el desarrollo de la aplicación web, con el propósito de mostrar la capacidad para manejar diversas tecnologías. A pesar de que la solución podría haberse implementado utilizando Python o Javascript tanto en el backend como en el frontend, se decidió emplear dos tecnologías específicas para desarrollo web, considerando las particularidades del puesto vacante.

## Instrucciones para correr el proyecto

Para correr el proyecto, sigue los siguientes pasos:

1. Clona este repositorio.
2. Asegúrate de tener instalado Python 3.8 o una versión superior.
3. Instala las dependencias del proyecto ejecutando `pip install -r requirements.txt` en la terminal.
4. Ejecuta `python manage.py migrate` para aplicar las migraciones y crear la base de datos.
5. Ejecuta `python manage.py runserver` para iniciar el servidor de desarrollo.
6. La API estará disponible en http://localhost:8000/. Puedes probar las vistas utilizando herramientas como Postman o desde el frontend desarrollado en Angular.

## API Endpoints

Los dos endpoints principales de la API son:

1. `/api/customers/`: Obtiene la lista de clientes, separados en dos grupos: repetidos y no repetidos.
2. `/api/reception_data/`: Permite cargar un archivo CSV y procesarlo, creando clientes y usuarios en la base de datos.

## GitHub Pages

El proyecto frontend se encuentra alojado en GitHub Pages y se puede acceder a él en https://melgyescas.github.io/FrontFullStackChallenge/

Recuerda que este archivo README corresponde al repositorio del backend. Para obtener información sobre el frontend, consulta el archivo README del repositorio de Angular [aquí](https://github.com/melgyescas/FrontFullStackChallenge/blob/main/README.md).
