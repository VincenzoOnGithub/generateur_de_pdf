from fpdf import FPDF
import os

### Créer la structure du PDF ###
class PDF(FPDF):
    def __init__(self, poste, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.poste = poste
        self.logo_path = "src/logo/logo_aforp.jpg"  ### Chemin du fichier logo ###

        ### Vérifiez que le fichier image existe ###
        if not os.path.isfile(self.logo_path):
            raise FileNotFoundError(f"Le fichier logo '{self.logo_path}' est introuvable.")

    def header(self):
        self.set_font('Arial', 'B', 12)
        ### Ajouter le logo en haut à droite ###
        try:
            self.image(self.logo_path, 160, 10, 30)  #
        except RuntimeError as e:
            raise RuntimeError(f"Erreur lors de l'ajout de l'image : {e}")
        self.cell(0, 10, self.poste, 0, 1, 'C')
        self.ln(10)

    def titre(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

### Ajouter le contenu du PDF ###
def generateur_cv(nom, prenom, poste, experiences, diplomes, competences):
    pdf = PDF(poste)
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f'Nom: {nom}', 0, 1)
    pdf.cell(0, 10, f'Prénom: {prenom}', 0, 1)
    
    pdf.ln(10)
    
    pdf.titre("Expériences Professionnelles:")
    pdf.body(experiences)
    
    pdf.titre("Diplômes:")
    pdf.body(diplomes)
    
    pdf.titre("Compétences:")
    pdf.body(competences)
    
    ### Générer le PDF au Nom et Prénom de l'utilisateur ###
    pdf.output(f"CV_{nom}_{prenom}.pdf")
