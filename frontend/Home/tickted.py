from reportlab.pdfgen import canvas
import os

def generar_ticket(pedido_id, mesa, total, items):
    archivo = f"ticket_{pedido_id}.pdf"
    c = canvas.Canvas(archivo)
    c.setFont("Helvetica", 12)

    c.drawString(50, 800, "BARISTAPOST - Ticket de Pedido")
    c.drawString(50, 780, f"Mesa: {mesa}")
    c.drawString(50, 760, f"Pedido ID: {pedido_id}")

    y = 740
    for item, precio in items:
        c.drawString(50, y, f"{item} - S/. {precio}")
        y -= 20

    c.drawString(50, y-20, f"Total: S/. {total}")
    c.showPage()
    c.save()

    os.startfile(archivo, "print")  # En Windows envía a imprimir
