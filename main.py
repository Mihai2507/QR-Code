import qrcode
import os
import sys

data = 'https://github.com/Mihai2507'
img = qrcode.make(data)
img_path = 'QR.png'
img.save(img_path)
os.startfile(img_path)
