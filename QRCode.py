import io
import pyqrcode
from base64 import b64encode
import eel

#eel inti (detecting web folder)
eel.init('web')


@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

#Generating Data when button get clicked and printing on console
@eel.expose
def generate_qr(data):
    img = pyqrcode.create(data)
    buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR code generation successful.")
    return "data:image/png;base64, " + encoded

# custom options
my_options = {
    'mode': "chrome-app",
    'host': 'localhost',
    'port': 8080
}

# eel starting html page with this size
eel.start('index.html', size=(1000, 600))
