from fpdf import FPDF
from datetime import datetime
import re

def remove_unicode(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

def create_pdf(advice, name="User", pie_img_path="pie.png", trend_img_path="trend.png"):
    pdf = FPDF()
    pdf.add_page()

    today = datetime.today().strftime('%d-%m-%Y')
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, remove_unicode(f"Name: {name}"), ln=True)
    pdf.cell(0, 10, f"Date: {today}", ln=True)

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, remove_unicode("AI Personal Finance Report"), ln=True, align='C')

    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, remove_unicode("Here is your personalized financial advice based on the data you provided:"))

    for tip in advice:
        safe_tip = remove_unicode(tip)
        pdf.multi_cell(0, 10, f"- {safe_tip}")

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Charts", ln=True)

    try:
        pdf.image(pie_img_path, x=30, w=150)
        pdf.ln(10)
        pdf.image(trend_img_path, x=30, w=150)
    except Exception as e:
        pdf.multi_cell(0, 10, remove_unicode(f"Could not add chart images: {e}"))

    pdf.output("financial_advice.pdf")
