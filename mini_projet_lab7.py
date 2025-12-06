
def moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)

def appliquer_bonus(notes, bonus=1):
    return [min(note + bonus, 20) for note in notes]

def filtrer_notes(notes, seuil):
    return [note for note in notes if note >= seuil]

def rapport(notes, bonus=1, seuil=12, titre="Rapport des notes"):
    notes_bonus = appliquer_bonus(notes, bonus)
    notes_valides = filtrer_notes(notes, seuil)

    lignes = [
        f"{titre}",
        f"Notes originales : {notes}",
        f"Notes bonus (+{bonus}) : {notes_bonus}",
        f"Moyenne initiale : {moyenne(notes):.2f}",  
        f"Moyenne bonus : {moyenne(notes_bonus):.2f}",
        f"Notes ≥ {seuil} : {notes_valides} (total {len(notes_valides)})"
    ]
    return "\n".join(lignes)

if __name__ == "__main__":
    notes = [12, 9, 15, 8, 17, 13, 19, 10]
    print("Rapport standard (paramètres par défaut):")
    print(rapport(notes))
    
    print("\n" + "="*50 + "\n")
    print("Rapport avancé (paramètres personnalisés):")
    print(rapport(notes, bonus=2, seuil=14, titre="Rapport avancé"))