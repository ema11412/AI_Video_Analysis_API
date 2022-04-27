import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import imagehash
import pandas as pd
import numpy as np
import json
import base64
import requests



#image

#pruebas 
dir0= '../../assets/'
dir = './application/assets'
#df = pd.read_csv("../../assets/data/values1.csv")
df = pd.read_csv(f"{dir}/data/values1.csv")

# prueba = 0

def alphaAnalysis(prueba):

    # t1 = f'{dir}/test/t{prueba}.jpg'
    ultVal = int(df["id"].iloc[-1][1:])

    # image = base64.b64decode(prueba)       
    # fileName = f'{dir}/test/in.jpg'
    # image_result = open(fileName , 'wb')
    # image_result.write(image)

    # response = requests.get(prueba)

    # file = open(f'{dir}/test/in.jpg', "wb")
    # file.write(response.content)
    #file.close()

    t1 = f'{dir}/test/in.jpg'

    # test image
    image = cv2.imread(t1)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])


    cs = []

    c1, c2 = 0, 0

    for i in range(ultVal+1):
        # data
        image = cv2.imread(f'{dir}/img/d{i}.jpg')        
        gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        histogram1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
        i = 0
        while i<len(histogram) and i<len(histogram1):
            c1+=(histogram[i]-histogram1[i])**2
            i+= 1
        c1 = c1**(1 / 2)
        cs += [c1[0]]

    ind = cs.index(min(cs))

    # hashing
    ahash1 = imagehash.average_hash(Image.open(t1)) 

    ahash0 = imagehash.average_hash(Image.open(f'{dir}/img/d{ind}.jpg')) 

    compHash = ahash1 - ahash0

    # calculo de alpha

    # valor de Umbral
    umbral = 20
    # Error de aproximación
    errorApr = ((umbral-compHash)/umbral)/10

    # valor de alpha referente a la imagen encontrada
    alpha0 = df[df['id']==f'd{ind}']['a']

    val = round(errorApr*alpha0+alpha0) 
    alpha = int(val.tolist()[0])

    # valor de lambda referente a la imagen encontrada
    lambda0 = df[df['id']==f'd{ind}']['lc']

    val = round(lambda0*errorApr+lambda0)
    lambdaa = int(val.tolist()[0])

    return alpha, lambdaa
