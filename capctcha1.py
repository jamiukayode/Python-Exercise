#pip install captcha   //8/8/2024
#pip install pillow

from captcha.image import ImageCaptcha

# Create a CAPTCHA image object
image = ImageCaptcha()

# Generate a CAPTCHA image with the text '1234'
data = image.generate('68y73Wos')

# # Save the image to a file
image.write('68y73Wos', 'captcha.png')


# data = image.generate('1234')
# image.write('1234', 'captcha.png')