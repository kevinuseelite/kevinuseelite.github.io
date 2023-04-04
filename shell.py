import argparse
import time
import logging
import os
import subprocess
from tqdm import tqdm
import var as v
import logging.handlers

start_time = time.time()

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a rotating file handler
handler = logging.handlers.RotatingFileHandler(v.logger, maxBytes=1024*1024, backupCount=5)
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


x = 1
if __name__ == '__main__':
    # Check if the output file already exists
    while x < 35000:
        print('instance:', x)
        if os.path.exists(v.output_file):
            logger.warning("Output file already exists and will be overwritten.")

        try:
            process = subprocess.Popen(["python", "app.py", ">", v.output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
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
        x+=1

    end_time = time.time()
    runtime = end_time - start_time
    logging.info(f"Script execution completed in {runtime:.2f} seconds.")
    print(f"Script execution completed in {runtime:.2f} seconds.")
