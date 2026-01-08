# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet

# def generate_pdf(report_text: str, output_path: str):
#     styles = getSampleStyleSheet()
#     doc = SimpleDocTemplate(output_path)

#     paragraphs = []
#     for line in report_text.split("\n"):
#         paragraphs.append(Paragraph(line, styles["Normal"]))

#     doc.build(paragraphs)

# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch

# def generate_report_pdf(report: dict, output_path: str):
#     """
#     Generates a PDF report from a structured report dictionary.

#     Args:
#         report (dict): The cleaned report dictionary from LLM.
#         output_path (str): Path where the PDF will be saved.
#     """
#     doc = SimpleDocTemplate(output_path, pagesize=A4)
#     styles = getSampleStyleSheet()
#     elements = []

#     # ----- Title -----
#     elements.append(Paragraph("Analytical Report", styles["Title"]))
#     elements.append(Spacer(1, 0.3 * inch))

#     # ----- Summary -----
#     elements.append(Paragraph("Summary", styles["Heading2"]))
#     summary = report.get("summary", "")

#     if isinstance(summary, dict):
#         summary_text = (
#             summary.get("overview")
#             or summary.get("overall_insight")
#             or "Summary not available"
#         )
#     else:
#         summary_text = summary or "Summary not available"

#     elements.append(Paragraph(summary_text, styles["Normal"]))
#     elements.append(Spacer(1, 0.3 * inch))

#     # ----- Key Metrics -----
#     elements.append(Paragraph("Key Metrics", styles["Heading2"]))
#     table_data = [["Metric", "Value"]]
#     key_metrics = report.get("key_metrics", {})
#     for key, value in key_metrics.items():
#         table_data.append([key.replace("_", " ").title(), str(value)])

#     if len(table_data) > 1:
#         table = Table(table_data, hAlign="LEFT")
#         elements.append(table)
#         elements.append(Spacer(1, 0.3 * inch))
#     else:
#         elements.append(Paragraph("No key metrics available.", styles["Normal"]))
#         elements.append(Spacer(1, 0.3 * inch))

#     # ----- Recommendations -----
#     elements.append(Paragraph("Recommendations", styles["Heading2"]))
#     recommendations = report.get("recommendations", {})
#     items = recommendations.get("action_items", [])

#     if isinstance(items, str):
#         elements.append(Paragraph(items, styles["Normal"]))
#     elif isinstance(items, list) and items:
#         for item in items:
#             elements.append(Paragraph(f"- {item}", styles["Normal"]))
#     else:
#         elements.append(Paragraph("No recommendations provided.", styles["Normal"]))

#     # ----- Build PDF -----
#     doc.build(elements)

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    ListFlowable,
    ListItem,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY


def generate_report_pdf(report: dict, output_path: str):
    """
    Generate a professional, business-ready PDF report from structured JSON.
    Trends & Recommendations are justified for better readability.
    """

    if not isinstance(report, dict):
        raise ValueError("Report must be a dictionary")

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()

    # -------- Justified paragraph style --------
    justified_style = ParagraphStyle(
        name="Justified",
        parent=styles["Normal"],
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )

    elements = []

    # =======================
    # Title
    # =======================
    elements.append(Paragraph("Analytical Business Report", styles["Title"]))
    elements.append(Spacer(1, 0.35 * inch))

    # =======================
    # Executive Summary
    # =======================
    elements.append(Paragraph("Executive Summary", styles["Heading2"]))

    summary = report.get("summary", "Summary not available")
    elements.append(Paragraph(str(summary), styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))

    # =======================
    # Key Metrics
    # =======================
    elements.append(Paragraph("Key Metrics", styles["Heading2"]))

    key_metrics = report.get("key_metrics", {})
    metric_rows = [["Metric", "Value"]]

    def format_value(val):
        if isinstance(val, (int, float)):
            return f"{val:,.2f}"
        return str(val)

    for key, value in key_metrics.items():
        label = key.replace("_", " ").title()

        if isinstance(value, dict):
            for sub_key, sub_val in value.items():
                sub_label = f"{label} – {sub_key.replace('_', ' ').title()}"
                metric_rows.append([sub_label, format_value(sub_val)])
        else:
            metric_rows.append([label, format_value(value)])

    table = Table(metric_rows, colWidths=[270, 200])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )

    elements.append(table)
    elements.append(Spacer(1, 0.35 * inch))

    # =======================
    # Trends & Correlations (JUSTIFIED)
    # =======================
    elements.append(Paragraph("Trends & Correlations", styles["Heading2"]))

    trends = report.get("trends_and_correlations", {})

    if isinstance(trends, dict) and trends:
        for key, description in trends.items():
            title = key.replace("_", " ").title()
            elements.append(
                Paragraph(
                    f"<b>{title}:</b> {description}",
                    justified_style,
                )
            )
            elements.append(Spacer(1, 0.12 * inch))
    else:
        elements.append(
            Paragraph(
                "No trends or correlations identified.",
                justified_style,
            )
        )

    elements.append(Spacer(1, 0.25 * inch))

    # =======================
    # Recommendations (JUSTIFIED)
    # =======================
    elements.append(Paragraph("Recommendations", styles["Heading2"]))

    recommendations = report.get("recommendations")
    bullet_items = []

    if isinstance(recommendations, dict):
        for title, text in recommendations.items():
            bullet_items.append(
                ListItem(
                    Paragraph(
                        f"<b>{title.replace('_', ' ').title()}:</b> {text}",
                        justified_style,
                    )
                )
            )

    elif isinstance(recommendations, list):
        for text in recommendations:
            bullet_items.append(
                ListItem(Paragraph(str(text), justified_style))
            )

    elif isinstance(recommendations, str):
        bullet_items.append(
            ListItem(Paragraph(recommendations, justified_style))
        )

    if bullet_items:
        elements.append(
            ListFlowable(
                bullet_items,
                bulletType="bullet",
                start="•",
                leftIndent=20,
            )
        )
    else:
        elements.append(
            Paragraph("No recommendations provided.", justified_style)
        )

    # =======================
    # Build PDF
    # =======================
    doc.build(elements)
