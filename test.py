import requests

# API_URL of your merge API
API_URL = 'http://localhost:8000/merge'

# Path to the zip file you want to send
FILE_PATH = 'Archive.zip'

# Open the file in binary mode and send it as part of a multipart-form data
with open(FILE_PATH, 'rb') as f:
    files = {'zip': (FILE_PATH, f, 'application/zip')}
    response = requests.post(API_URL, files=files,timeout=25)

# Check if the request was successful
if response.status_code == 200:
    # Save the received PDF to a file
    with open('output.pdf', 'wb') as out_file:
        out_file.write(response.content)
    print("PDF file saved as output.pdf")
else:
    print(f"Error: {response.status_code} - {response.text}")
