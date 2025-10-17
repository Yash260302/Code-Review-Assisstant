from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import subprocess
import os

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModelForSequenceClassification.from_pretrained("microsoft/codebert-base")

def analyze_code(code, language):
    feedback = []
    ignored_codes = {"W292", "E305", "W391"}

    if language.lower() == 'python':
        try:
            with open("temp_code.py", "w") as f:
                f.write(code)

            result = subprocess.run(
                ["flake8", "--select=E,W,F", "temp_code.py"],
                capture_output=True,
                text=True
            )
            if result.stdout.strip():
                for line in result.stdout.strip().splitlines():
                    parts = line.strip().split(":", 3)
                    if len(parts) != 4:
                        continue

                    _, lineno, col, message = parts
                    message_parts = message.strip().split(" ", 1)
                    if len(message_parts) != 2:
                        continue

                    code_id, description = message_parts
                    if code_id in ignored_codes:
                        continue

                    severity = (
                        "Error" if code_id.startswith("E")
                        else "Warning" if code_id.startswith("W")
                        else "Fatal"
                    )
                    formatted = f"Line {lineno}:{col}, {severity} Code - {code_id}: {description}"
                    feedback.append(formatted)

            if "TODO" in code:
                feedback.append("Code Quality Warning: Remove TODO comments before deployment.")

        except Exception as e:
            feedback.append(f"Error running flake8: {str(e)}")
    else:
        feedback.append("Analysis for this language is not supported. Only Python analysis is available.")
    if not feedback:
        feedback.append("No issues found. Your code looks good!")

    return feedback



@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'python')
    feedback = analyze_code(code, language)
    return jsonify({"feedback": feedback})


if __name__ == '__main__':
    app.run(port=5001)
