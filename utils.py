import os
import zipfile
import tempfile
from PyPDF2 import PdfWriter, PdfReader

def merger(files: list, basePath: str) -> str:
    pdfWriter = PdfWriter()
    for file in files:
        if file.endswith('.pdf'):
            with open(f'{basePath}/{file}', 'rb') as pdfFile:
                pdfFileObj = pdfFile
                pdfReader = PdfReader(pdfFileObj)
                for pageNum in range(len(pdfReader.pages)):
                    pageObj = pdfReader.pages[pageNum]
                    pdfWriter.add_page(pageObj)
                pdfFileObj.close()

    with open('merged.pdf', 'wb') as output_pdf:
        pdfWriter.write(output_pdf)
    return 'merged.pdf'

def unzipAndMerge(zipFile):
    with tempfile.TemporaryDirectory() as tempDir:
        with zipfile.ZipFile(zipFile, 'r') as zip_ref:
            zip_ref.extractall(tempDir)
            mergedPdfPath = merger(os.listdir(tempDir), tempDir)
            return mergedPdfPath
