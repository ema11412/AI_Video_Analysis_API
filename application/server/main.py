import uvicorn
from fastapi import FastAPI, File, UploadFile, Body
from starlette.responses import RedirectResponse

from application.components import predict, read_imagefile
from application.schema import Symptom
from application.components.prediction import symptom_check
from application.schema import Parameter
from application.components.ParamsPredict import paramsPredict, polyReg
from application.components.inputs import inputImage




app_desc = """<h2>Esta API provee una predicción de imagen digital utilizando machine learning</h2>
<h2>Esta optimizada para la prediccion de parametros del algoritmo EVM</h2>
<br>Emanuel Esquivel López"""

app = FastAPI(title='FastAPI EVM video analysis', description=app_desc)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    '''
        Código utilizado para la implementación de una red neuronal.
            NO UTILIZADO
            Podría ser de utilidad para el futuro....
    '''
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)

    return prediction



@app.get("/predict/parameter")
def ost_base64Image(base64_image: str):
    '''
        Consumido por la aplicacion android,
            No tiene una entrada significativa, ya que solo se usa un string input
            para validar el envio de datos.
        
        Input: 
            base64_image: String de comprobacion
        Output: 
            alp0 : Int -> Valor de alpha obtenido mediante analisis hash
            lamb0: Int -> Valor promedio entre hash y regrecion polinomial
    '''
    alpha, lambdaa = paramsPredict.alphaAnalysis(base64_image)

    poly_reg = polyReg.lambdaValue(alpha) 

    f_lambda = int((lambdaa+poly_reg)/2)

    if (f_lambda>2000):
        f_lambda = 1999

    return {"alp0": alpha, "lamb0": f_lambda//100}


@app.post("/predict/parameter")
def ost_base64Image(base64_image: str):
    '''
        Para pruebas locales.
        Se usa para analizar los parametros alpha y lambda

        Input: 
            base64_image: String de comprobacion
        Output: 
            alp0 : Int -> Valor de alpha obtenido mediante analisis hash
            lamb0: Int -> Valor promedio entre hash y regrecion polinomial
    '''
    alpha, lambdaa = paramsPredict.alphaAnalysis(base64_image)

    poly_reg = polyReg.lambdaValue(alpha) 

    f_lambda = int((lambdaa+poly_reg)/2)

    if (f_lambda>2000):
        f_lambda = 1999

    return {"alp0": alpha, "lamb0": lambdaa}



@app.post("/predict/input")
async def ost_base64Image(base64_image: str = Body(...)):
    '''
        Consumido por la aplicacion android,
            No tiene una entrada significativa, ya que solo se usa un string input
            para validar el envio de datos.
        
        Input: 
            base64_image: String con la imagen codificada en b64
                          enviada en el Body(...)
        Output: 
            0 : Sin especificar.
    '''    
    inputImage.inputImage(base64_image)

    return 0

if __name__ == "__main__":
    uvicorn.run(app, debug=True)