# Import QRCode library
import qrcode

# Set style and size
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

# Set a destination link/path/address
qr.add_data("https://www.linkedin.com/in/jay-vadgama")
qr.make(fit=True)

# Stylize the QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Set "save as" type and name
img.save("jayvadgama.png")
