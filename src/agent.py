import json
import os
from src.pdf_extractor import extract_text
from src.analyzer import analyze

OUTPUT_DIR = "output"
PDF_PATH = "Universal_Credit_Act_2025.pdf"  # relative to project root

def run_agent(pdf_path: str = PDF_PATH) -> dict:
    # 1. Extract text
    text = extract_text(pdf_path)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 2. Save extracted text (Task 1)
    extracted_path = os.path.join(OUTPUT_DIR, "extracted_text.txt")
    with open(extracted_path, "w", encoding="utf-8") as f:
        f.write(text)

    # 3. Analyze (Tasks 2–4)
    result = analyze(text)

    # 4. Save JSON
    json_path = os.path.join(OUTPUT_DIR, "final_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    return result


if __name__ == "__main__":
    res = run_agent()
    print("Analysis complete. JSON written to output/final_report.json")
