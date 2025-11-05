# Système de Gestion de Patients

Application simple en ligne de commande pour gérer des dossiers patients.

## Fonctionnalités

Ajouter un patient avec nom et date de naissance  
Consulter les détails d'un patient  
Ajouter des allergies  
Diagnostiquer avec codes ICD-10 validés  
Persistance des données en JSON

## Installation

1. **Téléchargez les fichiers** :

   - `patient_manager.py`
   - `codes.json`
   - `README.md`

2. **Lancez l'application** :

```bash
python3 patient_manager.py
```

## Utilisation

### Menu principal

```
--- Gestion des Patients ---
1. Ajouter un patient
2. Voir un patient
3. Ajouter une allergie
4. Diagnostiquer un patient
5. Quitter

```

### Exemple d'utilisation

```bash

$ python3 patient_manager.py

--- Gestion des Patients ---
1. Ajouter un patient
2. Voir un patient
3. Voir la liste des patients
4. Ajouter une allergie
5. Diagnostiquer un patient
6. Quitter

Choix : 1 Ajouter un patient
Nom complet : Khady DIAGNE
Date de naissance (AAAA-MM-JJ) : 1990-05-15
Patient ajouté avec ID 1

Choix : 3 Voir la liste des patients
Liste des patients :
ID: 1 - Khady DIAGNE (1990-05-15)
ID: 2 - Faty DIAGNE (2000-05-15)

Choix : 4 Ajouter une allergie
ID du patient : 1
Nom de l’allergie : Pénicilline
Allergie ajoutée

Choix : 5 Diagnostiquer un patient
ID du patient : 1
Code diagnostic (ex: A01) : J00
Diagnostic ajouté : J00 - Rhinopharyngite aiguë (rhume banal)

Choix : 2 Voir un patient
ID du patient : 1
{
    "nom": "Khady DIAGNE",
    "ddn": "1990-05-15",
    "allergies": ["Pénicilline"],
    "diagnostics": [
        {
            "code": "J00",
            "description": "Rhinopharyngite aiguë (rhume banal)"
        }
    ]
}

Choix : 6
Au revoir !

```

## Structure des fichiers

```
patient-manager/
├── patient_manager.py   # Application principale
├── codes.json           # Codes de diagnostic ICD-10
├── patients.json        # Données patients (créé automatiquement)
└── README.md            # Documentation

```

## Codes ICD-10 disponibles

| Code  | Description                                   |
| ----- | --------------------------------------------- |
| J00   | Rhinopharyngite aiguë (rhume banal)           |
| J06.9 | Infection des voies respiratoires supérieures |
| J45.0 | Asthme à prédominance allergique              |
| I10   | Hypertension essentielle (primaire)           |
| E11.9 | Diabète sucré de type 2, sans complication    |
| K21.9 | Reflux gastro-œsophagien sans œsophagite      |
| M54.5 | Lombalgie                                     |
| R50.9 | Fièvre, sans précision                        |
| A09   | Diarrhée et gastro-entérite                   |
| H10.9 | Conjonctivite, sans précision                 |

## Décisions de conception

### Simplicité du code

- Code court et facile à comprendre
- Fonctions simples avec un seul objectif
- Menu numérique intuitif

### Validation des diagnostics

- Les codes sont vérifiés dans `codes.json`
- Message d'erreur clair si le code n'existe pas
- Support des codes ICD-10 standards

### Persistance des données

- Sauvegarde automatique après chaque action
- Format JSON lisible et standard
- Chargement automatique au démarrage

## Format des données

### Structure d'un patient

```json
{
  "1": {
    "nom": "Fatou Sall",
    "ddn": "1990-05-15",
    "allergies": ["Pénicilline", "Arachides"],
    "diagnostics": [
      {
        "code": "J00",
        "description": "Rhinopharyngite aiguë (rhume banal)"
      }
    ]
  }
}
```

## Améliorations possibles

- Ajouter la modification/suppression de patients
- Générer des IDs uniques (UUID)
- Ajouter des tests unitaires
- Calculer l'âge automatiquement
- Exporter en PDF
- Interface graphique

## Auteur

KHADY DIAGNE
Développé dans le cadre d'un défi technique de recrutement.
