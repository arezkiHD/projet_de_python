from PIL import Image

# Load the image
input_image_path = r"C:\Users\arezk\Desktop\course\M1\Ipython\Projet_de_python\pictures\game_manipulation\\intr_pic.jpg"  # Replace with your image file name
output_image_path = "intro_pic.png"  # Output file name

try:
    # Open the image
    image = Image.open(input_image_path)  # Removed the extra comma

    # Resize the image to 30x10 (width x height)
    resized_image = image.resize((720,600), Image.Resampling.LANCZOS)

    # Save the resized image as a PNG
    resized_image.save(output_image_path, "PNG")

    print(f"Image resized and saved as {output_image_path}")
except FileNotFoundError:
    print(f"Error: The file '{input_image_path}' was not found. Please check the file path and name.")
except Exception as e:
    print(f"An error occurred: {e}")
