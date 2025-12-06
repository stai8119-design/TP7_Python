
def moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)

def appliquer_bonus(notes, bonus=1):
    return [min(note + bonus, 20) for note in notes]

def filtrer_notes(notes, seuil):
    return [note for note in notes if note >= seuil]

def min_max(notes):
    if not notes:
        return (None, None)
    return (min(notes), max(notes))

def normaliser(notes, max_original=20, sur=100):
    if max_original == 0:
        return [0.0] * len(notes)
        
    factor = sur / max_original
    return [round(note * factor, 2) for note in notes]

def generer_rapport(notes, max_original=20, bonus=1, seuil_validation=12, seuil_rattrapage=10):
    if not notes:
        return "Aucune note à traiter."
    NB_NOTES = len(notes)
    NOTES_MAX_NORMALISEE = 100
    SEUIL_VALIDATION_N = normaliser([seuil_validation], max_original, NOTES_MAX_NORMALISEE)[0]
    SEUIL_RATTRAPAGE_N = normaliser([seuil_rattrapage], max_original, NOTES_MAX_NORMALISEE)[0]
    
    notes_bonus = appliquer_bonus(notes, bonus)
    notes_normalisees = normaliser(notes_bonus, max_original, NOTES_MAX_NORMALISEE)
    notes_valides = filtrer_notes(notes_bonus, seuil_validation)
    
    min_max_notes = min_max(notes_bonus)
    top_3_notes = sorted(notes_bonus, reverse=True)[:3]

    validation = []
    rattrapage = []
    echec = []
    
    for note in notes_normalisees:
        if note >= SEUIL_VALIDATION_N:
            validation.append(note)
        elif note >= SEUIL_RATTRAPAGE_N:
            rattrapage.append(note)
        else:
            echec.append(note)
    
    lignes = [
        f"Rapport des notes",
        f"Nombre d'étudiants : {NB_NOTES}",
        f"Notes originales : {notes}",
        f"Notes après bonus (+{bonus}) : {notes_bonus}",
        f"Min/Max (après bonus) : {min_max_notes}",
        f"Top 3 des notes (après bonus) : {top_3_notes}",
        "",
        f"Moyenne initiale : {moyenne(notes):.2f}",
        f"Moyenne après bonus : {moyenne(notes_bonus):.2f}",
        f"Moyenne normalisée (sur {NOTES_MAX_NORMALISEE}) : {moyenne(notes_normalisees):.2f}",
        f"Notes >= {seuil_validation} (validées) : {len(notes_valides)} étudiants",
        "",
        f"Classification des notes (Normalisées sur {NOTES_MAX_NORMALISEE})",
        f"Validation (>= {SEUIL_VALIDATION_N:.2f}) : {len(validation)} étudiants",
        f"Rattrapage (>= {SEUIL_RATTRAPAGE_N:.2f}) : {len(rattrapage)} étudiants",
        f"Échec (< {SEUIL_RATTRAPAGE_N:.2f}) : {len(echec)} étudiants",
        "",
        f"Détails par étudiant (Sur {max_original} | Normalisé sur {NOTES_MAX_NORMALISEE}):"
    ]

    for index, note_originale in enumerate(notes, start=1):
        note_apres_bonus = notes_bonus[index - 1]
        note_normalisee = notes_normalisees[index - 1]
        
        categorie = ""
        if note_normalisee >= SEUIL_VALIDATION_N:
            categorie = "Validation"
        elif note_normalisee >= SEUIL_RATTRAPAGE_N:
            categorie = "Rattrapage"
        else:
            categorie = "Échec"

        lignes.append(
            f"Étudiant {index:02d} - Initiale: {note_originale:.2f}, Bonus: {note_apres_bonus:.2f}, Normalisée: {note_normalisee:.2f} ({categorie})"
        )

    return "\n".join(lignes)

def sauvegarder_rapport(contenu_rapport, nom_fichier="rapport_notes.txt"):
    try:
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(contenu_rapport)
        print(f"Rapport sauvegardé avec succès dans le fichier : {nom_fichier}")
    except IOError as e:
        print(f"Erreur lors de la sauvegarde du fichier : {e}")

if __name__ == "__main__":
    notes_originales = [12, 9, 15, 8, 17, 13, 19, 10]
    NOTE_MAX_ORIGINALE = 20 
   
    rapport_final = generer_rapport(
        notes=notes_originales, 
        max_original=NOTE_MAX_ORIGINALE,
        bonus=2, 
        seuil_validation=14, 
        seuil_rattrapage=10 
    )
    
    print("\n" + "="*50)
    print("Rapport généré et affiché dans la console :")
    print(rapport_final)
    print("="*50)
    
    sauvegarder_rapport(rapport_final)