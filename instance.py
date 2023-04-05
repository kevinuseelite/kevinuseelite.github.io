import subprocess
import time
import logging.handlers
import logging

def run_instance(x):
    counter = 0
    while counter < x:
        subprocess.run(["python", "shell.py"])
        counter+=1

if __name__ == '__main__':
    x = 10
    start_time = time.time()
    run_instance(x)
    end_time = time.time()
    runtime = end_time - start_time
    logging.info(f"Script execution completed in {runtime:.2f} seconds.")
    print(f"Script execution completed in ({runtime/60:.2f}) minutes.")