## About the application
<p style="font-size:18px">This is a Web Application writed with HTML/CSS & JS with backend Python<br><br>
You can generate a lot of QR Codes with this simple way you can add your text<br>
and after you clicking the button the image will apear.So you ready to scan.
<br>
You can scan in this <a href="https://online-barcode-reader.inliteresearch.com">website</a></p>
<b>If you want to download this application and run it directly without to change the code just click <a href="https://www.dropbox.com/s/3azisnn95hakjqp/QRCode.exe?dl=0">here</a>!
<img src='/qr1.png'>

## Getting Started
- Clone the repo and cd into the directory
```sh
$ git clone git@github.com:georgebak2182/qr-code-generator.git
$ cd qr-code-generator
```

- Install eel, pyqrcode, and pyinstaller

```sh
$ pip install eel pyqrcode pyinstaller pypng
```

- Run the app

```sh
$ python QRCode.py
```
## Packaging the app to .exe extension
python -m eel QRCode.py web --noconsole --onefile --icon barcode.ico<br>
<B>Check <a href="https://github.com/samuelhwilliams/Eel">EEL</a> how to pack the application if this way isn't working</b>
