import subprocess
import tqdm
import time
from tqdm import tqdm

if __name__ == '__main__':
    output_file = "C:/Users/kramos/Desktop/kevinuseelite.github.io/output.pdf"
    
    process = subprocess.Popen(["python", "app.py", ">", output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    with tqdm(total=100, desc="Converting to PDF", unit="%", unit_scale=True) as progress:
        for i in range(100):
            progress.update(1)
        time.sleep(0.000001)
    
    # Wait for the subprocess to finish
    process.communicate()
