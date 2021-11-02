from tika import parser

input_pdf = r'C:\Users\alanv\PythonCode\Projects\Inspired\Packing_List\90861.pdf'
parsed_pdf = parser.from_file(input_pdf)
print(parsed_pdf['content'])

# data = parsed_pdf['text']
# print(data)

# with open(input, 'rb') as f:
#     PDFfile = open("test.pdf", "rb")
#     pdfread = p2.PdfFileReader(PDFfile)

# x = pdfread.getPage(0)
# print(x.extractText())