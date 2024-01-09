import os
from flask import Flask, request, send_file
from utils import unzipAndMerge

app = Flask(__name__)


@app.route('/merge', methods=['POST'])
def merge():
    zipFile = request.files.get('zip')
    if zipFile:
        mergedPdfPath = unzipAndMerge(zipFile)

        if mergedPdfPath:
            response = send_file(mergedPdfPath, as_attachment=True)
            os.remove(mergedPdfPath)
            return response
    else:
        return {"STATUS": 400, "message": "No zip file provided"}

if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0", debug=True)
