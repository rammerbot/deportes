##### Español:
### Portal deportivo 
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20192843.png?raw=true" align="center" style="width: 100%" />
</div>  
  

### <div align="center">Pagina de Actualidades deportivas</div>  
  #### Descripcion.
  
> Trata de una web deportiva en donde se pueden visualizar los aconteceres mas acuales del mundo deportivo, asi como los resultado de los partidos, tanto locales como a nivel internacional.

#### Características
- pagina dinamica.
- Seccion por categoria.
- Seccion de noticias.
- Resultados.
- Publicidad.
- Actualidad.
- Panel administrativo.
- Cuenta de administrador.

#### Instalación

##### Crear entorno virtual:
```
python -m venv deportes
```

##### Entrar en el entorno
```
cd deportes
```
##### Activar el entorno dependiendo del sistema operativo
>  windows:
```
cd deportes/Script
```
```
activate
```
> en Lunix:
```
source deportes/bin/activate
```

##### Clonar el repositorio:

```
git clone https://github.com/rammerbot/deportes.git
```

> Navegar al directorio del proyecto:

```
cd deportes
```

##### Instalar las dependencias requeridas:

```
pip install -r requirements.txt
```

#### Uso
##### Crear base de dato y configurar la conexion
> luego ejecutar las migraciones
```
python manage.py makemigrations
```
```
python manage.py migrate
```

> Ejecutar la aplicación:

```
python manage.py runserver
```

##### Acceder al sistema a través de la URL proporcionada.

> Crear una cuenta de Administrador

```
python manage.py createsuperuser
```

##### Iniciar sesión con tu cuenta administrativa.
##### Usar la interfaz para cargar, evaluar y generar reportes y balances.

#### Contribuciones
##### Haz un fork del repositorio.

>Crea tu rama de funcionalidad:
  > Copiar código
```
git checkout -b feature/tu-funcionalidad
```
> Realiza tus cambios:

> Copiar código
```
git commit -m 'Agrega alguna funcionalidad'
```

> Sube tus cambios:

> Copiar código
```
git push origin feature/tu-funcionalidad
```
> Abre un pull request.
### Licencia
<p>Este proyecto está licenciado bajo la Licencia MIT. RammerBot</p>


### English:

## Caja System
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20192843.png?raw=true" align="center" style="width: 100%" />
</div>  
<div align="center">System for Centralizing Daily Report Flow</div>

 ### Description
 
 > It's a sport website where you can view the lasted happenings in the sport world, as well a macht results, both local and international.

#### Features

- Dynamic page.
- Section by category.
- News section.
- Results.
- Advertising.
- Current events.
- Administrative panel.
- Administrator account.
  
#### Installation
#### Create a virtual environment:

```
python -m venv deportes
```

#### Enter the environment
```
cd deportes
```
#### Activate the environment depending on the operating system:

> Windows:

```
cd deportes/Scripts
```
```
activate
```
> Linux:
```
source deportes/bin/activate
```

Clone the repository:
```
git clone https://github.com/rammerbot/deportes.git
```

> Navigate to the project directory:

```
cd deportes
```

#### Install the required dependencies:
```
pip install -r requirements.txt
```

#### Usage
#### Create a database and configure the connection

> Then run the migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

#### Run the application:

```
python manage.py runserver
```

#### Access the system through the provided URL.
 > Create an admin account:

```
python manage.py createsuperuser
```

#### Log in with your administrative account.
#### Use the interface to upload, evaluate, and generate reports and balances.
#### Contributions
> Fork the repository.
> Create your feature branch:

```
git checkout -b feature/your-feature
```

#### Commit your changes:

```
git commit -m 'Add some feature'
```

#### Push to the branch:
```
git push origin feature/your-feature
```

#### Open a pull request.

#### License
<p>This project is licensed under the MIT License. RammerBot</p>
