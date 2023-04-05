from distutils.cmd import Command
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging 
import logging.handlers 

logging.basicConfig(filename='variable_logger.log', level=logging.ERROR)

#set variables
output_file = "C:/Users/kramos/Desktop/kevinuseelite.github.io/output.pdf"
base_url = 'https://kevinuseelite.github.io/'
part_temp = 'index.html'
platform = 'win32'
cli_jar = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdfreactor.jar')
logger = 'myapp.log'
shell_in = 'python'
shell_out = 'app.py'
creds_path = "creds.txt"

# Variables to grab the images
img_dir = r"C:\Users\kramos\Desktop\kevinuseelite.github.io\images"
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
num_images = 0
img_paths = []
creds = {}

#values to store the database creds
def read_credentials_file(creds_file):
    try:
        with open(creds_file) as f:
            creds["db_name"] = f.readline().strip()
            creds["username"] = f.readline().strip()
            creds["password"] = f.readline().strip()
            creds["host"] = f.readline().strip()
            creds["port"] = 3306
        return creds
    except Exception as e:
        # Log the error
        logging.error("Error opening credentials file: {}".format(str(e)))
        raise e

read_credentials_file(creds_path)

#parses the image for the \dir
for filename in os.listdir(img_dir):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        # Get the full path to the image file
        file_path = os.path.join(img_dir, filename)
        # Append the image file path to the list
        img_paths.append(file_path)
