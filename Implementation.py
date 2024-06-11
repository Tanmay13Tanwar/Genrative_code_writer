from Reader import read_pdf,read_docx,read_csv,read_xlsx
from Writer import generate_code
from Executor import execute_code
from code_parser import parse_code

def interpret_file(file_path, file_type):
    if file_type == 'pdf':
        file_content = read_pdf(file_path)
    elif file_type == 'xlsx':
        file_content = read_xlsx(file_path)
    elif file_type == 'csv':
        file_content = read_csv(file_path)
    elif file_type == 'docx':
        file_content = read_docx(file_path)
    else:
        return "Unsupported file type"

    response = generate_code(file_content)
    code = parse_code(response)

    result = execute_code(code)
    return code,result