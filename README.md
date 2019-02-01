# Poll
En este proyecto a partir del Framework Django he creado una página web que muestra una pequeña encuesta conectada a una base de datos.
## Prerrequisitos
- Ubuntu-server 18.04
## Instalación
- Antes de todo Actualizamos --> **_sudo apt update y sudo apt upgrade_**.
En nuestro ubuntu server escribiremos la comanda **_"Python3  -V"_** para ver la versión de python que tenemos instalada.
Sinó tenemos la versión 3 de python la descargamos: **_"sudo apt install python3-pip"_** y **_"sudo apt install python3-venv"_**.
Ahora crearemos una carpeta donde estarán todos nuestros proyectos y entraremos en ella :**_"mkdir ~/newproject"_** para entrar en la carpeta pones la ruta **_"cd ~/newproject"_**.
- Zona virtual y descargando django:
crearemos una zona virtual y descargaremos django con pip: **_"python3.6 -m venv my_env"_** y para activar la zona virtual **_"source my_env/bin/activate"_**, todo esto dentro de la carpeta de nuestro proyecto, descargamos django --> **_"pip install django"_**, podemos verificar la instalación **_"django-admin --version"_**

- Proyecto nuevo y encendiendo server: primero de todo en el directorio donde está mnage.py pondremos la siguiente comanda **_python manage.py migrate_** para crear un proyecto **_"django-admin startproject mysite"_** en la carpeta newproject buscaremos el archivo settings.py dentro de este editaremos poniendo nuestra IP o * que permitirá todos los hosts **_ALLOWED_HOST =['*']_**.
Entramos en la carpeta mysite para encender el server --> **_"ufw allow 8000"_**  **_"python manage.py runserver nuestraIP:8000"_**. 
## Conectar Github
Conectaremos el proyecto creado anteriormente en nuestro ubuntu-server al github.
- Descargamos ---> **_apt-get install git"_**.
- Iniciamos sesión en git dentro del ubuntu --> **_git init_**, **_git config --global user.name "Tu nombre"_** y **_git config --global user.email "email"_**, podemos ver el estado de git con **_git status_**
- Añadimos repositorio y primer commit: git add **_"repositorio"_** y hacemos el commit **_git commit -m "mi primer commit"_**
- Ahora crearemos un repositorio desde la página web de github y nos dará un link, en el ubuntu server pondremos lo siguiente **_"git remote add origin "nuestro link""_**
- Hacemos el push **_git push -u origin master_**
