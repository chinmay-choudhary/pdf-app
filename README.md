# pdf-app

Flask app to merge multiple pdfs into one file

#### Setup and Running Instructions
* Step 1: Build the Docker Container
First, you need to build the Docker container. Open your terminal or command prompt and run the following command:

```bash
docker build -t <name-of-container> .
```
Replace <name-of-container> with your desired container name. This command builds a Docker image based on the Dockerfile in the current directory.

* Step 2: Run the Docker Container
After building the image, you can run the container using:

```bash
docker run -p <port:port> <name-of-container>
```
Replace <port:port> with the desired port mapping (e.g., 8080:8080). The format is host-port:container-port. Ensure the port you choose is free on your host machine.

Sample Request
```python

import requests

# URL of your merge API
url = 'http://localhost:8000/merge'

# Path to the zip file you want to send
file_path = 'path_to_your_zip_file.zip'

# Open the file in binary mode and send it as part of a multipart-form data
with open(file_path, 'rb') as f:
    files = {'zip': (file_path, f, 'application/zip')}
    response = requests.post(url, files=files)

# Check if the request was successful
if response.status_code == 200:
    # Save the received PDF to a file
    with open('output.pdf', 'wb') as out_file:
        out_file.write(response.content)
    print("PDF file saved as output.pdf")
else:
    print(f"Error: {response.status_code} - {response.text}")

```

To-Do
- Error Handling
- Add more features such as 'img to pdf', 'pdf to img', split pdf etc.