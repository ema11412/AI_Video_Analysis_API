import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse

from application.components import predict, read_imagefile
from application.schema import Symptom
from application.components.prediction import symptom_check
from application.schema import Parameter
from application.components.ParamsPredict import paramsPredict, polyReg





app_desc = """<h2>Esta API provee una predicción de imagen digital utilizando machine learning</h2>
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



@app.get("/predict/parameter")
def ost_base64Image(base64_image: str):
    # image = param.image
    alpha, lambdaa = paramsPredict.alphaAnalysis(base64_image)

    poly_reg = polyReg.lambdaValue(alpha) 

    f_lambda = int((lambdaa+poly_reg)/2)

    return {"alp0": alpha, "lamb0": f_lambda}


@app.post("/predict/parameter")
def ost_base64Image(base64_image: str):
    # image = param.image
    alpha, lambdaa = paramsPredict.alphaAnalysis(base64_image)

    poly_reg = polyReg.lambdaValue(alpha) 

    f_lambda = int((lambdaa+poly_reg)/2)

    return {"alp0": alpha, "lamb0": f_lambda}


if __name__ == "__main__":
    uvicorn.run(app, debug=True)


# http://127.0.0.1:8000/predict/parameter/{image_analisis}