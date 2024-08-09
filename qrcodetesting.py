# pip install qrcode // run this in your terminal 8/8/2024

import qrcode
# First method
img = qrcode.make('https://x.com/Ibrahim_webdev')
img.save('X.png')

#ypu  can generate as much as you want as you can see
img = qrcode.make('https://ibrahim-jamiu-portfolio.vercel.app/')
img.save('portfolio.png')


# second method
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QRCode object
qr.add_data('https://www.linkedin.com/in/ibrahim-jamiu-kayode-543509252?')
qr.make(fit=True)

# Create an image from the QRCode object
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save('linkedin.png')
