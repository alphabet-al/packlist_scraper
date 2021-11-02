from tika import parser

input_pdf = r'C:\Users\alanv\PythonCode\Projects\Inspired\Packing_List\96759.pdf'
parsed_pdf = parser.from_file(input_pdf)
# print(parsed_pdf)
print(parsed_pdf['content'])


