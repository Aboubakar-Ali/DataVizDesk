import tkinter as tk
from tkinter import filedialog, Toplevel, Label, Text, Scrollbar
from tkinter import messagebox
from extract import extract_metadata_and_first_chapter
from image import download_and_show_image
from viz import prompt_and_show_graph
from logo import rotate_and_save_logo
from word import generate_report

class BookManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de Livre")
        self.geometry("400x300")  
        self.setup_buttons()

    def setup_buttons(self):
        tk.Button(self, text="Extraire Livre", height=2, width=20, command=self.extract_book).pack(pady=10)
        tk.Button(self, text="Télécharger Image", height=2, width=20, command=self.download_image).pack(pady=10)
        tk.Button(self, text="Générer Graphique", height=2, width=20, command=self.generate_graph).pack(pady=10)
        tk.Button(self, text="Traiter Logo", height=2, width=20, command=self.process_logo).pack(pady=10)
        tk.Button(self, text="Générer Rapport Word", height=2, width=20, command=self.generate_word_report).pack(pady=10)

    def extract_book(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            title, author, first_chapter = extract_metadata_and_first_chapter(filepath)
            self.show_extraction_results(title, author, first_chapter)

    def show_extraction_results(self, title, author, first_chapter):
        result_window = Toplevel(self)
        result_window.title("Résultats de l'Extraction")
        result_window.geometry("400x300")  # Ajustez la taille selon le besoin

        # Bouton Menu en haut
        tk.Button(result_window, text="Menu", command=result_window.destroy).pack(side=tk.TOP, fill=tk.X)

        # Zone de texte avec défilement pour les résultats
        text_area = Text(result_window, height=10, width=50)
        scrollbar = Scrollbar(result_window, command=text_area.yview)
        text_area.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

         # Insertion des résultats dans la zone de texte
        text_area.insert(tk.END, f"Titre: {title}\nAuteur: {author}\nPremier Chapitre (Aperçu): {first_chapter}")

    def download_image(self):
        download_and_show_image(self)

    def generate_graph(self):
        prompt_and_show_graph()

    def process_logo(self):
        success, message = rotate_and_save_logo(self)
        if success:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)

    def generate_word_report(self):
        generate_report(self)

if __name__ == "__main__":
    app = BookManagementApp()
    app.mainloop()
