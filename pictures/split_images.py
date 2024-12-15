import pygame
import os
from PIL import Image


# Initialize Pygame
pygame.init()

# Dummy display (required for convert_alpha)
pygame.display.set_mode((1, 1))

# Load the sprite sheet
sprite_sheet = pygame.image.load(r"C:\Users\arezk\Desktop\course\M1\Ipython\Projet_de_python\monster.png").convert_alpha()

# Frame properties
num_columns = 7 # Number of frames in a row
num_rows = 5 # Number of rows in the sprite sheet

frame_width = 896/num_columns # Width of each frame
frame_height =896 / num_rows  # Height of each frame



# Output folder for frames
output_folder = r"C:\Users\arezk\Desktop\course\M1\Ipython\Projet_de_python\monster_4_direction"
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Extract and save frames
frame_count = 0
for row in range(num_rows):
    for col in range(num_columns):
        # Calculate the position of the frame in the sprite sheet
        x = col * frame_width
        y = row * frame_height

        # Extract the frame
        frame = sprite_sheet.subsurface((x, y, frame_width, frame_height))
        # to get the shape with 30x30
        frame = pygame.transform.smoothscale(frame, (30, 30))

        # Save the frame as a separate image
        frame_path = os.path.join(output_folder, f"frame_{frame_count}.png")
        pygame.image.save(frame, frame_path)
        print(f"Saved frame {frame_count} to {frame_path}")

        frame_count += 1

print("All frames extracted and saved!")
pygame.quit()
