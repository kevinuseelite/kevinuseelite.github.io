from distutils.cmd import Command
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#set variables
output_file = "C:/Users/kramos/Desktop/kevinuseelite.github.io/output.pdf"
base_url = 'https://kevinuseelite.github.io/'
part_temp = 'index.html'
platform = 'win32'
cli_jar = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdfreactor.jar')
logger = 'myapp.log'
shell_in = 'python'
shell_out = 'app.py'
creds = 'google_creds.txt'

# Variables to grab the images
img_dir = r"C:\Users\kramos\Desktop\kevinuseelite.github.io\images"
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
num_images = 0
img_paths = []

#values to store the database creds
lines = []
with open(creds) as f:
    lines = f.read().splitlines()


#parses the image for the \dir
for filename in os.listdir(img_dir):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        # Get the full path to the image file
        file_path = os.path.join(img_dir, filename)
        # Append the image file path to the list
        img_paths.append(file_path)
