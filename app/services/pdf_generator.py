# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet

# def generate_pdf(report_text: str, output_path: str):
#     styles = getSampleStyleSheet()
#     doc = SimpleDocTemplate(output_path)

#     paragraphs = []
#     for line in report_text.split("\n"):
#         paragraphs.append(Paragraph(line, styles["Normal"]))

#     doc.build(paragraphs)
