from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        # Rendering logo:
        pdf.image("C:/Users/Митя/Desktop/PythonProjects/Week8/shirtificate.png", x=-1, y=40)
        # Setting font: helvetica bold 48
        self.set_font("helvetica", "B", 48)
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

pdf = PDF()
pdf.add_page()
pdf.cell(180, 200, "Mitya took SC50", align='C')
pdf.set_text_color(0,0,0)
pdf.output("pdf-with-image.pdf")