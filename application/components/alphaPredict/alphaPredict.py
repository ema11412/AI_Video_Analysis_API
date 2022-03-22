import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import imagehash
import pandas as pd
import numpy as np
import json

#pruebas 
dir0= '../../assets/'
dir = './application/assets'
#df = pd.read_csv("../../assets/data/values1.csv")
df = pd.read_csv(f"{dir}/data/values1.csv")

#prueba = 0

def alphaAnalysis(prueba):
    t1 = f'{dir}/test/t{prueba}.jpg'
    ultVal = int(df["id"].iloc[-1][1:])

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

    # print(f"La imagen es comparable con {ind}")

    # fig, (ax1, ax2) = plt.subplots(1, 2)

    # A = mpimg.imread(f'{dir}/img/d{ind}.jpg')
    # B = mpimg.imread(t1)

    # ax1.imshow(B)
    # ax1.set_title('Imagen original')
    # ax2.imshow(A)
    # ax2.set_title("Imagen comparable")

    #plt.show()

    # hashing
    ahash1 = imagehash.average_hash(Image.open(t1)) 

    ahash0 = imagehash.average_hash(Image.open(f'{dir}/img/d{ind}.jpg')) 

    # ahash = df[df['id']==f'd{ind}']['ahash']
    # ahash0 = ahash.tolist()[0]
    # ahash1 = str(imagehash.average_hash(Image.open(t1)) )

    # print(type(ahash0))
    # print(type(ahash1))

    # print(ahash0)
    # print(ahash1)

    # print(hamming(ahash1,ahash0))

    compHash = ahash1 - ahash0

    # # calculo de alpha
    # valor de Umbral
    umbral = 20
    # Error de aproximación
    errorApr = abs((umbral-compHash)/umbral)/10

    # valor de alpha referente a la imagen encontrada
    alpha0 = df[df['id']==f'd{ind}']['a']

    val = round(errorApr*alpha0+alpha0)
    alpha = int(val.tolist()[0])

    # valor de lambda referente a la imagen encontrada
    lambda0 = df[df['id']==f'd{ind}']['lc']

    val = round(lambda0*errorApr+lambda0)
    lambdaa = int(val.tolist()[0])

    #response = {'alpha': alpha, 'lambda' : lambdaa}
    #print(f'El valor de alpha es {alpha}, y lambda {lambdaa}')

    return alpha, lambdaa


#prueba = 0
#print(alphaAnalysis(prueba))