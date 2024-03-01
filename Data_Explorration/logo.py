# logo.py
from tkinter import filedialog, simpledialog
from PIL import Image


def rotate_and_save_logo(window):
    # Demander à l'utilisateur de sélectionner le fichier logo
    logo_path = filedialog.askopenfilename(title="Sélectionnez l'image du logo")
    if logo_path:
        # Demander à l'utilisateur d'entrer l'angle de rotation
        angle = simpledialog.askinteger("Rotation", "Entrez l'angle de rotation du logo:", minvalue=0, maxvalue=360)
        if angle is not None:
            try:
                with Image.open(logo_path) as logo:
                    rotated_logo = logo.rotate(angle, expand=True)
                    save_path = 'Data Explorration/Image/Photo1.png'
                    rotated_logo.save(save_path)
                    return True, "Le logo a été pivoté et enregistré avec succès."
            except Exception as e:
                return False, f"Erreur lors de la rotation et de la sauvegarde de l'image : {e}"
    return False, "Opération annulée par l'utilisateur ou fichier non sélectionné."
