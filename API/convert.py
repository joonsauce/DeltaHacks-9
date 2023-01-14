import base64

def convert(data):
    image = base64.b64decode(data)
    file = 'image.png'
    with open(file, 'wb') as f:
        f.write(image)