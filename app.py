from flask import Flask, request, send_file
from flask_cors import CORS
from utils.utils import unzipAndMerge
import os
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)



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
            return {"STATUS": 500, "message": "Failed to merge PDFs"}
    else:
        return {"STATUS": 400, "message": "No zip file provided"}

if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0", debug=True)
