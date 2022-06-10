# Curso FastAPI con SQL Alchemy
https://www.youtube.com/watch?v=6eVj33l5e9M&t=1s&ab_channel=FaztCode

https://www.youtube.com/watch?v=_eWEmRWhk9A&ab_channel=FaztCode

```
conda activate fastapi01
```

## Preparar entorno virtual
    
### Anaconda 
(https://www.youtube.com/watch?v=aE7qxfgubS8&ab_channel=Fazt)
```
conda info
conda create --name [nombre del enviroment] python=3.5
conda activate [nombre del enviroment]
conda deactivate
conda env list
conda install [paquete de python] // Igual que pip install
conda env remove --name [nombre del enviroment]
```
- Crear y activar el entorno virtual de python
- Seleccionar el entorno virtual de python ctrl + P "> python select

### fastApi y uvicorn
```
pip install fastapi uvicorn

uvicorn [filename]:[objeto] --reload
uvicorn app:app --reload
```

### sqlAlchemy
Docs: https://docs.sqlalchemy.org/en/14/core/tutorial.html#version-check
```
pip install sqlalchemy pymysql cryptography
```

#### Crear Base de datos con docker
engine = create_engine("mysql+pymysql://root:fastapiPass@localhost:3306/storedb")

```
 docker run --detach --name fastapi-mariadb -v C:\Users\franc\Documents\Cursos\FastAPI_SQLAlchemy_fazt\datadb:/var/lib/mysql -e MARIADB_ROOT_PASSWORD=fastapiPass -e MARIADB_DATABASE=storedb -e MARIADB_MYSQL_LOCALHOST_USER=1 -p 3306:3306 -d mariadb:latest
```