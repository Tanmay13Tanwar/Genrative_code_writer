import re
def parse_code(code):

    pattern = re.compile(r"```python(.*?)```",re.DOTALL)
    match=pattern.search(code)
    if match:
        return match.group(1).strip()
    else:
        return ''