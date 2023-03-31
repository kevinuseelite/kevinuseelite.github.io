import subprocess

# Specify the absolute path of the output file
output_file = "C:/Users/kramos/Desktop/kevinuseelite.github.io/output.pdf"

# Execute the command to generate the PDF file
subprocess.run(["python", "app.py", ">", output_file], shell=True)
