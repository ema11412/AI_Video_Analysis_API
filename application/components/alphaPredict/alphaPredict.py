import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import imagehash
import pandas as pd
import numpy as np

df = pd.read_csv("../../assets/data/values1.csv")

prueba = 3

t1 = f'../../assets/test/t{prueba}.jpg'
ultVal = int(df["id"].iloc[-1][1:])

# test image
image = cv2.imread(t1)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

cs = []

c1, c2 = 0, 0

for i in range(ultVal+1):
    # data
    image = cv2.imread(f'../../assets/img/d{i}.jpg')
    gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histogram1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    i = 0
    while i<len(histogram) and i<len(histogram1):
        c1+=(histogram[i]-histogram1[i])**2
        i+= 1
    c1 = c1**(1 / 2)
    cs += [c1[0]]

ind = cs.index(min(cs))

print(f"La imagen es comparable con {ind}")

fig, (ax1, ax2) = plt.subplots(1, 2)


A = mpimg.imread(f'../../assets/img/d{ind}.jpg')
B = mpimg.imread(t1)

ax1.imshow(B)
ax1.set_title('Imagen original')
ax2.imshow(A)
ax2.set_title("Imagen comparable")

plt.show()


# hashing
hash0 = imagehash.average_hash(Image.open(t1)) 
hash1 = imagehash.average_hash(Image.open(f'../../assets/img/d{ind}.jpg')) 
compHash = hash0 - hash1


# calculo de alpha
alpha0 = df[df['id']==f'd{ind}']['a']

val = round((compHash**2/100)+alpha0)
alpha = val.tolist()[0]

print(alpha)

