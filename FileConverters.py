import PyPDF2
import docx2txt
import docx
from fpdf import FPDF
from ErrorLogging import LogError

#Convert PDF Doc
def pdf2_to_text(path):
    #uses package pypdf2
    text = ""
    #opens pdf
    try:
        pdfFileObj = open(path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
    except (PyPDF2.utils.PdfReadError, PyPDF2.utils.PdfReadWarning) as err:
        LogError(err, path)
        
    else:
        #Reads pdf page by page
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            text += pageObj.extractText()
                    
    return text

#Convert PDF Doc to a list
def pdf2_to_list(fileName):
    text = []
    #opens pdf and read it
    pdfFileObj = open(fileName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
    #Reads pdf page by page
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        text.append(pageObj.extractText())

    return text

#Convert DOCX to text
def docx2_to_txt(path):
    #Uses package docx2txt
    text = ""
    
    try:
        text = docx2txt.process(path)
    except Exception as err:
        LogError(err, path)
    
    return text

#Convert DOCX to list
def docsx_to_list(path):
    # open connection to Word Document
    doc = docx.Document(path)
    
    # read in each paragraph in file
    text = [p.text for p in doc.paragraphs]

    return text

#Convert Text File to PDF
def txtFile_to_pdf(filename):
    # save FPDF() class into a variable pdf 
    pdf = FPDF() 

    # Add a page 
    pdf.add_page() 

    # set style and size of font that you want in the pdf 
    pdf.set_font("Arial", size = 8)

    try: 
        # open the text file in read mode with special encoding for special characters
        f = open(filename, "r", encoding='utf-8')
        line = f.read()

        #Encode the text so that special characters can be used
        line = line.encode('latin-1', 'ignore').decode('latin-1')

        # insert the texts in pdf 
        pdf.multi_cell(200, 5, line, 0, 1)

    except Exception as err:
            LogError(err, filename)
    else:
        try:
            # save and output the pdf
            pdf.output("Data.pdf", 'F')
        except Exception as err:
            LogError(err, "Data.pdf")
