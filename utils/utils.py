from PyPDF2 import PdfWriter, PdfReader
import zipfile
import tempfile
import os

def merger(files: list, basePath: str) -> str:
    try:
        pdfWriter = PdfWriter()

        for file in files:
            if file.endswith('.pdf'):
                pdfFileObj = open(f'{basePath}/{file}', 'rb')  # Open each of the file paths in the files list.
                pdfReader = PdfReader(pdfFileObj)  # Read each of the files.
                for pageNum in range(len(pdfReader.pages)):
                    pageObj = pdfReader.pages[pageNum]  # Get each page
                    pdfWriter.add_page(pageObj)  # Add each page to the writer object

                pdfFileObj.close()

        with open('merged.pdf', 'wb') as output_pdf:
            pdfWriter.write(output_pdf)
        
        return 'merged.pdf'
    except Exception as e:
        print(f'{e}')
        return 'None'

def unzipAndMerge(zipFile):
    with tempfile.TemporaryDirectory() as tempDir:
        with zipfile.ZipFile(zipFile, 'r') as zip_ref:
            zip_ref.extractall(tempDir)
            mergedPdfPath = merger(os.listdir(tempDir), tempDir)

            return mergedPdfPath


