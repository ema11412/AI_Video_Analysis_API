import base64


dir0= '../../assets/'
dir = './application/assets'


def inputImage(prueba):

    image = base64.b64decode(prueba)       
    fileName = f'{dir}/test/in.jpg'
    image_result = open(fileName , 'wb')
    image_result.write(image)