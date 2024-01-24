import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://choyonuddin.github.io/resume/Choyon%20Resume%20October.pdf')
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save("TestQR.png")