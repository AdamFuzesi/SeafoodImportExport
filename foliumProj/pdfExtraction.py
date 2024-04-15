import pandas as pd
import numpy as np
import pdfplumber

textContent = []

with pdfplumber.open("/Users/adifuzesi/Desktop/PythonProjects/foliumProj/CanadaSeafoodImportExport.pdf") as pdf:
    for page in pdf.pages:
        textContent.append(page.extract_text())

print(textContent[0][:500])


with open('output.txt', 'w') as f:
    for text in textContent:
        f.write(text + '\n')


