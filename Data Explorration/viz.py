# viz.py
import re
from collections import Counter
import matplotlib.pyplot as plt
from tkinter import filedialog, messagebox

def read_first_chapter(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    chapter_content = re.search(r'CHAPTER I([\s\S]*?)(?=CHAPTER II|APPENDIX)', text)
    return chapter_content.group(1) if chapter_content else "Contenu du premier chapitre non trouvé."

def analyse_distribution_paragraphes(filepath):
    text_chapitre = read_first_chapter(filepath)
    paragraphs = [para for para in text_chapitre.split('\n') if para.strip()]
    word_counts = [round(len(re.findall(r'\w+', para))/10)*10 for para in paragraphs]
    distribution = Counter(word_counts)
    sorted_distribution = sorted(distribution.items())
    return sorted_distribution

def show_graph(sorted_distribution):
    plt.figure(figsize=(10, 6))
    plt.bar([str(x[0]) for x in sorted_distribution], [x[1] for x in sorted_distribution], color='skyblue')
    plt.xlabel('Nombre de Paragraphes')
    plt.ylabel('Nombre de Mots arrondi à la dizaine')
    plt.title('Distribution des Longueurs des Paragraphes du Premier Chapitre')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def prompt_and_show_graph():
    filepath = filedialog.askopenfilename(title="Sélectionnez un fichier de livre")
    if not filepath:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné.")
        return

    sorted_distribution = analyse_distribution_paragraphes(filepath)
    if sorted_distribution:
        show_graph(sorted_distribution)
    else:
        messagebox.showerror("Erreur", "Impossible de générer le graphique du premier chapitre.")
