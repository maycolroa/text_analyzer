![logopython](https://github.com/user-attachments/assets/30173a6c-2700-4567-8190-27e24c27f8ee)

## Description

Este proyecto es una aplicación web que permite realizar diversas operaciones de análisis de texto, como contar palabras, invertir texto, contar caracteres, y más. La aplicación está dividida en un frontend y un backend, los cuales están ejecutados y configurados con Docker para simplificar el despliegue.

## Proyecto de Análisis de Texto

- Descripción del Proyecto

- Estructura del Proyecto

- Configuración de Docker

- Explicación del Backend

- Explicación del Frontend

- Cómo Ejecutar el Proyecto

- Explicación del Proceso de Análisis


## Descripción del Proyecto

- La aplicación de Análisis de Texto permite al usuario realizar varias operaciones sobre un texto ingresado. A través de un frontend desarrollado con Vue.js, el usuario puede seleccionar diferentes opciones de análisis y ver los resultados en tiempo real. El backend, desarrollado con FastAPI, procesa el texto y realiza los cálculos solicitados por el frontend. Ambas aplicaciones están configuradas para ejecutarse en contenedores Docker, lo que facilita su despliegue en cualquier sistema que soporte Docker.

![image](https://github.com/user-attachments/assets/8415700d-a679-42c8-92dc-80f599445898)

## Estructura del Proyecto

![image](https://github.com/user-attachments/assets/25505ea7-d54c-4ebc-8bd3-1520c9eefb7f)

## Configuración de Docker

Docker se utiliza para crear y ejecutar contenedores que contengan el backend y el frontend de la aplicación. Esto asegura que la aplicación se ejecute en un entorno controlado, eliminando conflictos de dependencias y permitiendo una fácil portabilidad.

Archivo docker-compose.yml
El archivo docker-compose.yml permite ejecutar el frontend y el backend simultáneamente. Define dos servicios:

Backend: Ejecuta el servidor de FastAPI en el puerto 8000.
Frontend: Ejecuta la aplicación de Vue.js servida por nginx en el puerto 8080.

archivo docker-compose.yml
```
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    env_file:
      - ./backend/.env
    ports:
      - "8000:8000"
    volumes:
      - ./backend/app:/app/app
    depends_on:
      - frontend

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "8080:80"
    environment:
      - VITE_API_URL=http://localhost:8000  # URL del backend
```

## Explicación del Backend

El backend está desarrollado en Python usando FastAPI, un framework web rápido y moderno que permite construir APIs de manera sencilla.

- main.py: Este archivo es el punto de entrada de la aplicación de FastAPI. Configura la API y establece los parámetros de CORS (Cross-Origin Resource Sharing) para permitir que el frontend acceda a la API.

- Controlador (text_analyzer.py): El controlador gestiona las rutas que reciben las solicitudes desde el frontend. Aquí es donde se define la lógica para los endpoints de análisis de texto, los cuales llaman a servicios específicos para procesar el texto.

- Servicios (text_service.py): Este archivo contiene la lógica principal de procesamiento de texto. Utiliza los métodos de cadenas de Python para contar palabras, invertir texto, buscar palabras específicas, etc.

- Modelos (request_models.py): Este archivo define los modelos de datos usados en las solicitudes y respuestas. Permite a FastAPI validar los datos entrantes de manera sencilla.

## Explicación del Frontend

El frontend está desarrollado con Vue.js y se encarga de la interfaz gráfica con la que interactúa el usuario.

- App.vue: El componente principal de la aplicación, que sirve como contenedor para el componente de análisis de texto.

- TextAnalyzer.vue: Este componente contiene la lógica de la interfaz. Proporciona botones para cada una de las operaciones de análisis (contar palabras, invertir texto, contar caracteres, etc.). Usa Axios para enviar las solicitudes al backend y mostrar los resultados.

- Estilos: Utiliza Tailwind CSS para aplicar estilos a los botones y la interfaz de usuario, haciendo que la aplicación se vea moderna y responsiva.

## Cómo Ejecutar el Proyecto

```bash

$ git clone https://github.com/tu_usuario/text_analyzer.git

$ cd text_analyzer

```

```bash

$ docker-compose up --build

```

Accede a la Aplicación:

- Frontend: Abre un navegador y ve a http://localhost:8080.
- Backend: La API de FastAPI está disponible en http://localhost:8000/docs#/.


## Sigueme

- Author - [maycol roa](https://www.linkedin.com/in/maycol-david-roa-trivi%C3%B1o-14b27a106/)
- Website - [portafolio](https://maycol.webflow.io/about)

