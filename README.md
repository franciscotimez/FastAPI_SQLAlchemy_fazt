# Curso FastAPI con SQL Alchemy
https://www.youtube.com/watch?v=6eVj33l5e9M&t=1s&ab_channel=FaztCode

https://youtu.be/6eVj33l5e9M?t=732

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