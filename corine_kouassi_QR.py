import qrcode

url = "https://codeforcorine.github.io/QR-Code-cate-de-visite/"

img = qrcode.make(url)
img.save("qr_corine_contact.png")