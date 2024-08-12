from PIL import Image

# Load the Mona Lisa image
image_path = 'Desafios\Torta_CERP.jpg'  # Path to the Mona Lisa image
original_image = Image.open(image_path)

# Resize the image to create a pixelated effect
pixel_size = 10  # Size of the pixels in the pixelated image
small_image = original_image.resize(
    (original_image.width // pixel_size, original_image.height // pixel_size), 
    Image.NEAREST
)
pixelated_image = small_image.resize(original_image.size, Image.NEAREST)

# Display the pixelated image
pixelated_image.show()

# Save the pixelated image
pixelated_image.save('pixelated_mona_lisa.png')