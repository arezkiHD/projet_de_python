
################################################################################################
##################################### FOR ONE PICTURE ##########################################

#from PIL import Image
#
## Load the image
#input_image_path = r"C:\Users\arezk\Desktop\course\M1\Ipython\Projet_de_python\pictures\game_manipulation\\intr_pic.jpg"  # Replace with your image file name
#output_image_path = "intro_pic.png"  # Output file name
#
#try:
#    # Open the image
#    image = Image.open(input_image_path)  # Removed the extra comma
#
#    # Resize the image to 30x10 (width x height)
#    resized_image = image.resize((30,30), Image.Resampling.LANCZOS)
#
#    # Save the resized image as a PNG
#    resized_image.save(output_image_path, "PNG")
#
#    print(f"Image resized and saved as {output_image_path}")
#except FileNotFoundError:
#    print(f"Error: The file '{input_image_path}' was not found. Please check the file path and name.")
#except Exception as e:
#    print(f"An error occurred: {e}")
#







##########################################################################################################
##################################### FOR MANY PICTURES ###################################################





from PIL import Image
import os

# Directory coC:\Users\arezk\Desktop\course\M1\Ipython\Projet_de_python\pictures\4direction_chara\monster_4_direction
input_dir = r"C:\Users\arezk\Desktop\course\M1\Ipython\Projet_de_python\pictures\4direction_chara\monster_4_direction"
output_dir = r"C:\Users\arezk\Desktop\course\M1\Ipython\Projet_de_python\pictures\4direction_chara\monster_4_direction\res"
os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

# Loop through images 1 to 16
for i in range(1, 17):
    # Construct the input image path. 
    # Adjust the naming pattern to match your actual files.
    # For example, if your images are named intr_pic_1.jpg, intr_pic_2.jpg, etc.:
    input_image_path = os.path.join(input_dir, f"monster ({i}).png")

    # Construct the output image path
    output_image_path = os.path.join(output_dir, f"monster_res{i}.png")

    try:
        # Open the image
        image = Image.open(input_image_path)

        # Resize the image to 30x30
        resized_image = image.resize((30, 30), Image.Resampling.LANCZOS)

        # Save the resized image as a PNG
        resized_image.save(output_image_path, "PNG")

        print(f"Image {i} resized and saved as {output_image_path}")
    except FileNotFoundError:
        print(f"Error: The file '{input_image_path}' was not found. Please check the file path and name.")
    except Exception as e:
        print(f"An error occurred processing {input_image_path}: {e}")
