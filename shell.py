import subprocess
import logging
import tkinter as tk
from tkinter import filedialog

logging.basicConfig(level=logging.INFO)

class PDFConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("PDF Converter")
        master.geometry("500x300")
        master.config(bg="black")

        self.label = tk.Label(master, text="Output File Name:", bg="black", fg="white")
        self.label.pack()

        self.output_file_entry = tk.Entry(master)
        self.output_file_entry.pack()

        self.output_file_button = tk.Button(master, text="Select Output Folder", bg="darkgreen", fg="white", command=self.select_output_folder)
        self.output_file_button.pack(pady=10)

        self.convert_button = tk.Button(master, text="Convert to PDF", bg="darkgreen", fg="white", command=self.convert_to_pdf)
        self.convert_button.pack(pady=10)

        self.exit_button = tk.Button(master, text="Exit", bg="darkgreen", fg="white", command=master.quit)
        self.exit_button.pack(pady=10)

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()

    def convert_to_pdf(self):
        output_file = self.output_folder + "/" + self.output_file_entry.get() + ".pdf"

        # Check if the output file already exists
        if os.path.exists(output_file):
            logging.warning("Output file already exists and will be overwritten.")

        try:
            process = subprocess.Popen(["python", "app.py", ">", output_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        except (OSError, subprocess.SubprocessError) as e:
            logging.error(f"Error: {e}")
            exit(1)

        # Wait for the subprocess to finish
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            logging.error(f"Error: Subprocess failed with code {process.returncode}.")
            exit(1)

        # Check if the output file has been created successfully
        if os.path.exists(output_file):
            logging.info(f"Output file {output_file} created successfully.")
        else:
            logging.error(f"Error: Output file {output_file} not created.")
            exit(1)

root = tk.Tk()
gui = PDFConverterGUI(root)
root.mainloop()
