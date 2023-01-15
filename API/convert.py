import base64
def convert(data):
    image = base64.b64decode(data)
    file = 'image.jpg'
    with open(file, 'wb') as f:
        f.write(image)