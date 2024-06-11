from Implementation import interpret_file

file_path = 'timezone.docx'  # Replace with your file path
file_type = 'docx'  # The type of the file (pdf, xlsx, csv, docx)

code,execution_output = interpret_file(file_path, file_type)
print("code: \n",code,'\n\n\n',"execution output: \n",execution_output)