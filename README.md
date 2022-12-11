# Proyecto final Unidad 03 - Curso MTPE Backend, Silabuz

Este proyecto usa datos extraídos de <https://rickandmortyapi.com/> que se cargan en una base de datos MongoDB almacenada de forma local.

En esta aplicación se pueden ver los personajes de la serie, ya sea en forma de páginas o el perfil de cada uno. Los perfiles contienen enlaces a los episodios.

## Instalación

---

- Debes tener instalado el lenguaje Python (con la libreria pip) y la base de datos MongoDB.
- Descarga el código del repositorio GitHub (.zip) o clónalo a través de la terminal:

```
  >git clone https://github.com/akajar/proyectoU03-personajes.git
```

- Crea un entorno virtual de Python:

```
  >python -m venv env
```

- Ejecuta el script "activate":
  - Windows:  
  
  ```
    >.\env\Scripts\activate
  ```

  - Linux / Mac:
  
  ```
    $source env/bin/activate
  ```

- Instala las dependencias dentro de "requirements.txt"

```
>pip install -r requirements.txt
```

- Inicia la conexión de MongoDB en otra terminal:

```
>mongod
```

- Inicia la aplicación:

```
>flask run
```