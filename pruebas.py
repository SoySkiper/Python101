from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

def merge_png_to_pdf(png_file1, png_file2, output_pdf):
    # Crear un archivo PDF con tamaño de página carta (oficio)
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)

    # Lista para almacenar los elementos que se añadirán al PDF
    elements = []

    # Leer los archivos PNG y añadirlos al PDF
    for png_file in [png_file1, png_file2]:
        img = Image(png_file, width=letter[0], height=letter[1])
        elements.append(img)

    # Construir el PDF
    doc.build(elements)

if __name__ == "__main__":
    png_file1 = "/home/soyskiper/Descargas/page_1.png"   # Ruta del primer archivo PNG
    png_file2 = "/home/soyskiper/Descargas/page_1.png"   # Ruta del segundo archivo PNG
    output_pdf = "/home/soyskiper/Descargas/Acta_Nacimiento.pdf"  # Ruta del archivo PDF de salida

    merge_png_to_pdf(png_file1, png_file2, output_pdf)
