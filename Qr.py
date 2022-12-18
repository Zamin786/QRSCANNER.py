import qrcode
img = qrcode.make(
    'https://www.facebook.com/zamin.sheikh.3133'
)
img.save('myQRcode.png')
img.show()