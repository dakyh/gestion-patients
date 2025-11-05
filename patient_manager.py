import json
# Fichiers 
DATA_FILE = "patients.json"
CODES_FILE = "codes.json"

# Chargement des données 
def charger_donnees():
    try:
        with open(DATA_FILE, "r",encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

# Sauvegarde des données entrer
def sauvegarder_donnees(donnees):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4,ensure_ascii=False)

# Chargement du codes de diagnostic enter
def charger_codes():
    try:
        with open(CODES_FILE, "r",encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

# Ajout d'un nouveau patient
def ajouter_patient():
    donnees = charger_donnees()
    nom = input("Nom complet : ")
    ddn = input("Date de naissance (AAAA-MM-JJ) : ")
    nouvel_id = str(len(donnees) + 1)
    donnees[nouvel_id] = {
        "nom": nom,
        "ddn": ddn,
        "allergies": [],
        "diagnostics": []
    }
    sauvegarder_donnees(donnees)
    print(f" Patient ajouté avec ID {nouvel_id}")

# Voir un patient
def voir_patient():
    donnees = charger_donnees()
    pid = input("ID du patient : ")
    if pid in donnees:
        print(json.dumps(donnees[pid], indent=4, ensure_ascii=False))
    else:
        print(" Patient introuvable.")
        
# liste de tous les patient
def voir_tous_les_patients():
    donnees = charger_donnees() 
    if len(donnees) == 0:
        print(" Aucun patient enregistré.")
        return
    print("\n================= LISTE DE TOUS LES PATIENTS =================")
    print(f"{'ID':<5} {'Nom':<30} {'Date de naissance':<20} {'Allergies':<10}")
    print("-" * 65)
    
    for pid, patient in donnees.items():
        nom = patient["nom"]
        ddn = patient["ddn"]
        nb_allergies = len(patient["allergies"])
        
        print(f"{pid:<5} {nom:<30} {ddn:<20} {nb_allergies:<10}")    
    print(f"Total : {len(donnees)} patient(s)\n")

# Ajouter une allergie
def ajouter_allergie():
    donnees = charger_donnees()
    pid = input("ID du patient : ")
    if pid in donnees:
        allergie = input("Nom de l'allergie : ")
        donnees[pid]["allergies"].append(allergie)
        sauvegarder_donnees(donnees)
        print(" Allergie ajoutée.")
    else:
        print(" Patient introuvable.")

# Diagnostiquer un patient
def diagnostiquer_patient():
    donnees = charger_donnees()
    codes = charger_codes()
    pid = input("ID du patient : ")
    if pid not in donnees:
        print(" Patient introuvable.")
        return
    code = input("Code diagnostic (ex: A01) : ").upper()
    if code in codes:
        description = codes[code]
        donnees[pid]["diagnostics"].append({"code": code, "description": description})
        sauvegarder_donnees(donnees)
        print(f" Diagnostic ajouté : {code} - {description}")
    else:
        print(" Code inconnu. Veuillez vérifier le fichier codes.json")

# Menu principal
def menu():
    while True:
        print("\n--- Gestion des Patients ---")
        print("1. Ajouter un patient")
        print("2. Voir un patient")
        print("3. Voir tous les patients")  
        print("4. Ajouter une allergie")
        print("5. Diagnostiquer un patient")
        print("6. Quitter")
        
        choix = input("Choix : ")
        if choix == "1":
            ajouter_patient()
        elif choix == "2":
            voir_patient()
        elif choix == "3":
             voir_tous_les_patients()
        elif choix == "4":
            ajouter_allergie()
        elif choix == "5":
            diagnostiquer_patient()
        elif choix == "6":
            print(" Au revoir !")
            break
        else:
            print(" Choix invalide.")

if __name__ == "__main__":
    menu()
