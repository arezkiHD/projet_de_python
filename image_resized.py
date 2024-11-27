from PIL import Image

# Load the image
input_image_path = "grass.png"  # Replace with your image file name
output_image_path = "grass.png"  # Output file name

# Open the image
image = Image.open(input_image_path)

# Resize the image to 64x32 (width x height)
resized_image = image.resize((30, 30), Image.Resampling.LANCZOS)

# Save the resized image as a PNG
resized_image.save(output_image_path, "PNG")

print(f"Image resized and saved as {output_image_path}")
