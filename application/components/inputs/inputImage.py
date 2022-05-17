import base64

# Direcciones utilziadas.
#   Las referencias son acorde a uviconr................................*
dir0= '../../assets/'
dir = './application/assets'


def inputImage(prueba):
    '''
        Se encarga de realizar el guardado de la imagen

            Input:
                - prueba: String con la imagen en base64_image
            Output:
                - None
    '''
    image = base64.b64decode(prueba)       
    fileName = f'{dir}/test/in.jpg'
    image_result = open(fileName , 'wb')
    image_result.write(image)