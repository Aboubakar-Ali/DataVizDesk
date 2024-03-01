import re

def extract_metadata_and_first_chapter(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Extraction du titre, de l'auteur
    title_search = re.search(r'Title:\s*(.+)', text)
    author_search = re.search(r'Author:\s*(.+)', text)
    title = title_search.group(1) if title_search else 'Titre inconnu'
    author = author_search.group(1) if author_search else 'Auteur inconnu'
    
    # Extraction et aperçu du premier chapitre
    first_chapter_search = re.search(r'(CHAPTER [IVXLCDM]+.*?)(?=CHAPTER [IVXLCDM]+|$)', text, re.DOTALL)
    first_chapter = first_chapter_search.group(1).strip()[:50] if first_chapter_search else 'Chapitre non trouvé'
    
    return title, author, first_chapter

# filepath = 'Data Explorration/livre.txt'
# title, author, first_chapter = extract_metadata_and_first_chapter(filepath)
# print(f"Titre: {title}\nAuteur: {author}\nPremier Chapitre (Aperçu): {first_chapter}")