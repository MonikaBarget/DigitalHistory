import pyfpdf

html_source="C:\\Users\\mbarg\\Downloads\\IWHSO_supply_depots.html"

pdf = pyfpdf.FPDF(format='image')
pdf.add_page()
pdf.cell(200, 10, img=html_source)
pdf.output("C:\\Users\\mbarg\\Downloads\\IWHSO_supply_depots.pdf")
