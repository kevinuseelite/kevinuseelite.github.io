import argparse
import time
import logging
import os
import subprocess
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm
import var as v
import logging.handlers
import pymysql
import warnings 
from django.http import HttpResponse
from django.shortcuts import render


start_time = time.time()
# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

with warnings.catch_warnings():
    warnings.simplefilter(action='ignore', category=FutureWarning)

# create a rotating file handler
handler = logging.handlers.RotatingFileHandler(v.logger, maxBytes=1024*1024, backupCount=5)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

# Extract the credentials from the list.
try:
    conn = pymysql.connect(
        host =          'iuseeliteparts.cswkkvpqnjji.us-east-1.rds.amazonaws.com',
        user =          'partmaster',
        password =      'Partmaster123Partmaster123',
        port=           3306,
        cursorclass=    pymysql.cursors.DictCursor

  )
    logger.info("Successfully connected to MySQL server")

except pymysql.err.OperationalError as e:
    if e.args[0] == 1044:
        logger.error("Access denied for user")
    elif e.args[0] == 1045:
        logger.error("Invalid username or password")
    elif e.args[0] == 2003:
        logger.error("Could not connect to MySQL server")
    else:
        logger.error("Error connecting to MySQL: %s", str(e))
    exit()
except pymysql.Error as e:
    logger.error("Error connecting to MySQL: %s", str(e))
    exit()

# Check if the output file already exists
if os.path.exists(v.output_file):
    logger.warning("Output file already exists and will be overwritten.")

def run_script():
    try:
        process = subprocess.Popen([v.shell_in, v.shell_out, ">", v.output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        with tqdm(total=100, desc="Converting to PDF", unit="%", unit_scale=True) as progress:
            for i in range(100):
                progress.update(1)
        # Wait for the subprocess to finish
        stdout, stderr = process.communicate(timeout=10)
        if process.returncode != 0:
            logger.error(f"Error: Subprocess failed with code {process.returncode}.")
            logging.error(f"stdout: {process.stdout.read().decode()}")
            logging.error(f"stderr: {process.stderr.read().decode()}")
            exit(1)
        else:
            # Check if the output file has been created successfully
            logger.info(f"Output file {v.output_file} created successfully.")
    except (OSError, subprocess.SubprocessError, subprocess.TimeoutExpired) as e:
        logger.error(f"Error: {e}")
        logging.error(f"stdout: {process.stdout.read().decode()}")
        logging.error(f"stderr: {process.stderr.read().decode()}")
        exit(1)

run_script()

end_time = time.time()
runtime = end_time - start_time
logging.info(f"Script execution completed in {runtime:.2f} seconds.")
print(f"Script execution completed in {runtime:.2f} seconds.")