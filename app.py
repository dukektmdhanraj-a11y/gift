from flask import Flask, request, send_file
from docxtpl import DocxTemplate
import os

app = Flask(__name__)

# Base directory of project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 🔹 Home page — loads Gift form
@app.route("/")
def home():
    return open(
        os.path.join(BASE_DIR, "html", "gift.html"),
        encoding="utf-8"
    ).read()


# 🔹 Generate Gift Report
@app.route("/generate_gift", methods=["POST"])
def generate_gift():
    # Collect form data
    data = request.form.to_dict()

    # Path to Word template
    template_path = os.path.join(
        BASE_DIR,
        "templates_docx",
        "gift.docx"
    )

    # Render-safe temporary save location
    output_path = "/tmp/gift_report.docx"

    # Generate document
    doc = DocxTemplate(template_path)
    doc.render(data)
    doc.save(output_path)

    # Send file to browser
    return send_file(output_path, as_attachment=True)


# 🔹 Run locally
if __name__ == "__main__":
    app.run(debug=True)
