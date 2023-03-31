#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys

# You can download the PDFreactor Web Service Python client from: 
# http://www.pdfreactor.com/download/get/?product=pdfreactor&type=webservice_clients&jre=false
from PDFreactor import *

# Create new PDFreactor instance
pdfReactor = PDFreactor()

# Set the base URL for all relative links in the HTML document
base_url = 'https://kevinuseelite.github.io/'

# Create a new PDFreactor configuration object
config = {
    # Specify the input document
    'document': base_url + 'index.html',

    # Set the base URL for all relative links in the HTML document
    'baseURL': base_url,


}

# The resulting PDF
result = None

try: 
    # Render document and save result
    result = pdfReactor.convertAsBinary(config)
except PDFreactorWebserviceException as e:
    # Not successful, print error and log
    print("Content-type: text/html\n\n")
    print("<h1>An Error Has Occurred</h1>")
    print("<h2>"+str(e)+"</h2>")
    
# Check if successful
if result != None:
    # Used to prevent newlines are converted to Windows newlines (\n --> \r\n) 
    # when using Python on Windows systems 
    if sys.platform == "win32":
        import msvcrt
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
    
    # Set the correct header for PDF output and offer as download
    print("Content-Disposition: attachment; filename=output.pdf")
    print("Content-Type: application/pdf\n")
    
    # Write PDF content to standard output
    sys.stdout.flush()
    sys.stdout.buffer.write(result)
