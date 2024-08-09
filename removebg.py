# pip install rembg
from rembg import remove
from PIL import Image

# Load the input image
input_path = 'plane.jpeg'  # Replace with your image path
output_path = 'plane.png'

# Open the image
inp = Image.open(input_path)

# Remove the background
output = remove(inp)

# Save the result
output.save(output_path)
print(f"Background removed. Saved as {output_path}")


