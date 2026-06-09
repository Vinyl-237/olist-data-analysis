from pathlib import Path

# Racine du projet
BASE_DIR = Path(__file__).parent.parent # Chemin vers le dossier du projet

# Chemins vers les dossiers de données
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
INTERRIM_DIR = DATA_DIR / "iterim"
PROCESSED_DIR = DATA_DIR / "processed"

# Chemins vers les fichiers de données utils
NOTEBOOKS_DIR = BASE_DIR / "notebooks"
REPORTS_DIR = BASE_DIR / "REPORTS"
FIGURES_DIR = REPORTS_DIR / "figures"
EXPORTS_DIR = REPORTS_DIR / "exports"

# Affichons les chemins pour vérification
print(f"Dossier général du projet: {BASE_DIR}")
print(f"Chemin général des données: {DATA_DIR}")
print(f"Dossier des données brutes: {RAW_DIR}")
print(f"Dossier des données intermédiaires: {INTERRIM_DIR}")
print(f"Dossier des données traitées: {PROCESSED_DIR}")
print(f"Dossier des notebooks: {NOTEBOOKS_DIR}")
print(f"Dossier des rapports: {REPORTS_DIR}")
print(f"Dossier des figures: {FIGURES_DIR}")
print(f"Dossier des exports: {EXPORTS_DIR}")