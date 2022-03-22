import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse

from application.components import predict, read_imagefile
from application.schema import Symptom
from application.components.prediction import symptom_check

app_desc = """<h2>Esta API provee una prediccion de imagen digital utilizando machine learning</h2>
<h2>Esta optimizada para la prediccion de parametros del algoritmo EVM</h2>
<br>Emanuel Esquivel López"""

app = FastAPI(title='FastAPI EVM video analysis', description=app_desc)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)

    return prediction


@app.post("/api/covid-symptom-check")
def check_risk(symptom: Symptom):
    return symptom_check.get_risk_level(symptom)


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
