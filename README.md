# AI_Video_Analysis_API
Video analysis with machine learning 

## Install
```
pip install -r requirements.txt
```

## Run

```
uvicorn --host 0.0.0.0 --port 5000 application.server.main:app --reload
```

* `--host` indica la dirección donde se aloja el API.
* `--port` establece el puerto.
* `--reload` permite que durante el **desarrollo**, el API se actualice cuando se guarden los cambios.

## Rutas

Se pueden ver las rutas:
```
    http://localhost:5000/
```