import PyPDF2
from typing import Union, IO

def extract_text(file_or_path: Union[str, IO[bytes]]) -> str:
    """
    Works with:
    - A file path string (for agent.py)
    - A Streamlit UploadedFile object (file-like)
    """

    # CASE 1 — When a path string is provided
    if isinstance(file_or_path, str):
        try:
            f = open(file_or_path, "rb")
            reader = PyPDF2.PdfReader(f, strict=False)
            text = ""
            for page in reader.pages:
                try:
                    t = page.extract_text() or ""
                    text += t + "\n"
                except:
                    continue
            f.close()
            return text
        except Exception as e:
            return f"[PDF Error: {e}]"

    # CASE 2 — When a Streamlit UploadedFile is provided
    try:
        reader = PyPDF2.PdfReader(file_or_path, strict=False)
        text = ""
        for page in reader.pages:
            try:
                t = page.extract_text() or ""
                text += t + "\n"
            except:
                continue
        return text

    except Exception as e:
        return f"[PDF Error: {e}]"
