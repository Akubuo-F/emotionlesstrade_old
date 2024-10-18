from src.app.utils.base.abstract_pdf_generator import AbstractPDFGenerator

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class PDFGenerator(AbstractPDFGenerator):

    @staticmethod
    def cot_report_calculation(pdf_filename: str) -> None:
        page: canvas.Canvas = canvas.Canvas(pdf_filename, pagesize=letter)
        width, height = letter

        page.drawString(72, height - 72, "COT Report Calculations:")
        page.drawString(72, height - 100, "1. Percentage Change Long:")
        page.drawString(100, height - 120, "Percentage Change Long = (Long Change / (Current Long + Previous Long)) * 100")

        page.drawString(72, height - 150, "2. Percentage Change Short:")
        page.drawString(100, height - 170,
                     "Percentage Change Short = (Short Change / (Current Short + Previous Short)) * 100")

        page.drawString(72, height - 200, "3. Percentage Change Net:")
        page.drawString(100, height - 220,
                     "Percentage Change Net = ((Current Net - Previous Net) / (|Current Net| + |Previous Net|)) * 100")

        page.drawString(72, height - 250, "4. Percentage Change Open Interest:")
        page.drawString(100, height - 270,
                     "Percentage Change Open Interest = (Open Interest Change / Current Open Interest) * 100")

        # Example values to illustrate
        page.drawString(72, height - 300, "Example:")
        page.drawString(100, height - 320, "Current Long = 1000, Previous Long = 900")
        page.drawString(100, height - 340, "Current Short = 500, Previous Short = 450")
        page.drawString(100, height - 360, "Current Open Interest = 1500, Open Interest Change = 200")

        page.drawString(100, height - 390, "Percentage Change Long = round((100 / 1900) * 100, 1) ≈ 5.3%")
        page.drawString(100, height - 410, "Percentage Change Short = round((50 / 950) * 100, 1) ≈ 5.3%")
        page.drawString(100, height - 430, "Percentage Change Net = round((50 / 950) * 100, 1) ≈ 5.3%")
        page.drawString(100, height - 450, "Percentage Change Open Interest = round((200 / 2800) * 100, 1) ≈ 7.1%")

        # summary
        page.drawString(72, height - 480, "Summary:")
        page.drawString(100, height - 500, "Sometimes the percentages being equal can seem counter-intuitive.")
        page.drawString(100, height - 520, "All changes (percentage long change, percentage short change, and percentage net")
        page.drawString(100, height - 540, "change) are indeed 5.3%. This results because both long and short values have changed")
        page.drawString(100, height - 560, "by the same relative amount (100 units for long and 50 units for short) in this particular")
        page.drawString(100, height - 580, "scenario.")

        page.save()
        return


if __name__ == '__main__':
    PDFGenerator.cot_report_calculation("cot_report_formulas.pdf")