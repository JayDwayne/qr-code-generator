import qrcode

# Initialize QRCode object
qr = qrcode.QRCode(
    version=None,  # set to None so that version is automatically determined
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

# Add data to the QRCode object and generate QR code data
qr.add_data('Bruce')
qr.make(fit=True)

# Generate QR code image using default color scheme 
img = qr.make_image()

# Output image in PNG format
img.save("bruce.png")
