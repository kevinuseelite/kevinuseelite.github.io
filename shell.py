import subprocess
import tqdm
import time
import logging
from tqdm import tqdm

logging.basicConfig(filename='myapp.log', level=logging.INFO)

if __name__ == '__main__':
    output_file = "C:/Users/kramos/Desktop/kevinuseelite.github.io/output.pdf"

    try:
        process = subprocess.Popen(["python", "app.py", ">", output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    except (OSError, subprocess.SubprocessError) as e:
        logging.error(f"Error: {e}")
        exit(1)

    with tqdm(total=100, desc="Converting to PDF", unit="%", unit_scale=True) as progress:
        for i in range(100):
            progress.update(1)
        time.sleep(0.000001)

    # Wait for the subprocess to finish
    try:
        stdout, stderr = process.communicate(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        logging.error("Error: Subprocess timed out.")
        exit(1)

    if process.returncode != 0:
        logging.error(f"Error: Subprocess failed with code {process.returncode}.")
        exit(1)
