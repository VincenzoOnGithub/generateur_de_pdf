import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from cv_generateur import generateur_cv

### Interface graphique pour récolter les informations ###
class CVApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Générateur de CV")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Nom:").grid(row=0, column=0, padx=10, pady=5)
        self.nom = tk.Entry(self.root)
        self.nom.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Prénom:").grid(row=1, column=0, padx=10, pady=5)
        self.prenom = tk.Entry(self.root)
        self.prenom.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Nom du Poste:").grid(row=2, column=0, padx=10, pady=5)
        self.poste = tk.Entry(self.root)
        self.poste.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Expériences Professionnelles:").grid(row=3, column=0, padx=10, pady=5)
        self.experience = scrolledtext.ScrolledText(self.root, width=40, height=10)
        self.experience.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Diplômes:").grid(row=4, column=0, padx=10, pady=5)
        self.diplomes = scrolledtext.ScrolledText(self.root, width=40, height=5)
        self.diplomes.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Compétences:").grid(row=5, column=0, padx=10, pady=5)
        self.competences = scrolledtext.ScrolledText(self.root, width=40, height=5)
        self.competences.grid(row=5, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Générer CV", command=self.generateur_cv).grid(row=6, column=0, columnspan=2, pady=10)
    
    ### Fonction pour stocker les informations ###
    def generateur_cv(self):
        nom = self.nom.get()
        prenom = self.prenom.get()
        poste = self.poste.get()
        experiences = self.experience.get("1.0", tk.END).strip()
        diplomes = self.diplomes.get("1.0", tk.END).strip()
        competences = self.competences.get("1.0", tk.END).strip()

        if not (nom and prenom and poste and experiences and diplomes and competences):
            messagebox.showwarning("Erreur", "Attention : tous les champs doivent être remplis !")
            return

        ### Bouton pour générer le CV ###
        generateur_cv(nom, prenom, poste, experiences, diplomes, competences)
        messagebox.showinfo("Succès", f"Bravo {prenom}, votre CV a été généré !")

    def run(self):
        self.root.mainloop()
