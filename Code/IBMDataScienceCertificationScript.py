import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://choyonuddin.github.io/Resume/resume.pdf')
qr.make(fit=True)

img = qr.make_image(fill_color="White", back_color="black")

img.save("ResumeQR.Jpeg")