from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logo_path = "generateur_de_cv/src/logo/logo_aforp.jpg"  # Chemin du fichier logo

    def header(self):
        self.set_font('Arial', 'B', 12)
        # Ajouter le logo en haut à droite
        self.image(self.logo_path, 160, 10, 30)  # (x, y, width)
        self.cell(0, 10, 'Curriculum Vitae', 0, 1, 'C')
        self.ln(10)

    def titres(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generateur_cv(nom, prenom, experiences, diplomes, competences):
    pdf = PDF()
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f'Nom: {nom}', 0, 1)
    pdf.cell(0, 10, f'Prénom: {prenom}', 0, 1)
    
    pdf.ln(10)
    
    pdf.titres("Expériences Professionnelles:")
    pdf.body(experiences)
    
    pdf.titres("Diplômes:")
    pdf.body(diplomes)
    
    pdf.titres("Compétences:")
    pdf.body(competences)
    
    pdf.output(f"CV_{nom}_{prenom}.pdf")
