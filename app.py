from flask import Flask, request, send_file
from docxtpl import DocxTemplate
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def home():
    return open(os.path.join(BASE_DIR, "html", "gift.html"), encoding="utf-8").read()


@app.route("/generate_gift", methods=["POST"])
def generate_gift():
    data = request.form.to_dict()

    template_path = os.path.join(BASE_DIR, "templates_docx", "gift.docx")

    # IMPORTANT: Render-safe save location
    output_path = "/tmp/gift_report.docx"

    doc = DocxTemplate(template_path)
    doc.render(data)
    doc.save(output_path)

    return send_file(output_path, as_attachment=True)


if __name__ == "__main__":
    app.run()
