import sys
import io

def execute_code(code):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    try:
        exec(code)
        output = redirected_output.getvalue()
    except Exception as e:
        output = str(e)
    finally:
        sys.stdout = old_stdout
    return output