@app.route("/gift")
def gift_form():
    return open(os.path.join(BASE_DIR, "html", "gift.html")).read()


@app.route("/generate_gift", methods=["POST"])
def generate_gift():
    data = request.form.to_dict()

    template_path = os.path.join(BASE_DIR, "templates_docx", "gift.docx")
    output_path = os.path.join(BASE_DIR, "gift_report.docx")

    doc = DocxTemplate(template_path)
    doc.render(data)
    doc.save(output_path)

    return send_file(output_path, as_attachment=True)