from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def gerar_pdf(resumo):
    pdf = canvas.Canvas("output/relatorio.pdf", pagesize=A4)
    largura, altura = A4

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, altura - 50, "Relatório de Vendas")

    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, altura - 100, f"Total registros: {resumo['total_registros']}")
    pdf.drawString(50, altura - 130, f"Média: {resumo['media']:.2f}")
    pdf.drawString(50, altura - 160, f"Máximo: {resumo['maximo']}")
    pdf.drawString(50, altura - 190, f"Mínimo: {resumo['minimo']}")

    pdf.save()