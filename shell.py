import time
import logging
import os
import subprocess
from tqdm import tqdm
import var as v

start_time = time.time()
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # Check if the output file already exists
    if os.path.exists(v.output_file):
        logging.warning("Output file already exists and will be overwritten.")

    try:
        process = subprocess.Popen(["python", "app.py", ">", v.output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        with tqdm(total=100, desc="Converting to PDF", unit="%", unit_scale=True) as progress:
            for i in range(100):
                progress.update(1)
           # time.sleep(0.000001)
        # Wait for the subprocess to finish
        stdout, stderr = process.communicate(timeout=10)
        if process.returncode != 0:
            logging.error(f"Error: Subprocess failed with code {process.returncode}.")
            exit(1)
        else:
            # Check if the output file has been created successfully
            logging.info(f"Output file {v.output_file} created successfully.")
    except (OSError, subprocess.SubprocessError, subprocess.TimeoutExpired) as e:
        logging.error(f"Error: {e}")
        exit(1)

    end_time = time.time()
    runtime = end_time - start_time