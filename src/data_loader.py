# Ici nous allons créer des fonction pour charger et résumer les informations sur nos données
import pandas as pd
from pathlib import Path
from src.config import RAW_DIR

def get_csv_files(data_dir = RAW_DIR):
    """
    Retourne la liste des fichiers csv présents dans le dossier des données brutes (raw).
    """
    return sorted(data_dir.glob("*.csv"))

def clean_table_name(file_path: Path) -> str:
    """
    Transforme le nom d'un fichier comme olist_orders_dataset.csv en orders.
    """
    name = file_path.stem # Récupère le nom du fichier sans l'extension
    name = name.replace("olist_", "") # Supprime le préfixe "olist_
    name = name.replace("_dataset", "") # Supprime le suffixe "_dataset"
    return name

def load_csv(file_path: Path) -> pd.DataFrame:
    """
    Charge un fichier csv dans un DataFrame pandas.
    """
    return pd.read_csv(file_path)

def load_all_tables(data_dir = RAW_DIR) -> dict:
    """
    Charge tous les fichiers csv du dossier des données brutes (raw) et les retourne dans un dictionnaire.
    Les clés du dictionnaire sont les noms des tables nettoyés (ex: "orders", "customers", etc.).
    """
    tables = {}
    for file_path in get_csv_files(data_dir): # Parcourt tous les fichiers csv du dossier
        table_name = clean_table_name(file_path) # Nettoie le nom du fichier pour obtenir le nom de la table
        tables[table_name] = load_csv(file_path) # Charge le fichier csv dans un DataFrame et l'ajoute au dictionnaire
    return tables

def get_table_overview(df: pd.DataFrame, table_name: str) -> dict:
    """
    Retourne un résumé simple d'une table
    """
    return {
        "table": table_name,
        "n_rows": df.shape[0],
        "n_cols": df.shape[1],
        "missing_cells": int(df.isna().sum().sum()), # Nombre total de cellules manquantes le .sum() deux fois pour faire la somme sur les lignes puis sur les colonnes
        "duplicate_rows": int(df.duplicated().sum()) # Nombre de lignes dupliquées
    }

def build_overview_table(tables: dict) -> pd.DataFrame:
    """
    Construit une table de résumé pour toutes les tables chargées.
    """
    overview = [
        get_table_overview(df, name) # Crée un résumé pour chaque table et l'ajoute à la liste
        for name, df in tables.items() # Parcourt chaque table et construit un résumé pour chacune
    ]
    return pd.DataFrame(overview).sort_values("n_rows", ascending=False) # Trie la table de résumé par nombre de lignes décroissant