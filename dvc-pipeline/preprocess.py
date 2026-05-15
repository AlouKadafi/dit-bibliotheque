import json
import pandas as pd
from pathlib import Path

# Création du dossier data si nécessaire
Path("dvc-pipeline/data").mkdir(parents=True, exist_ok=True)

# Chargement des données JSON
with open("dvc-pipeline/data/loans.json", "r", encoding="utf-8-sig") as f:
    raw = json.load(f)

# Extraction des données
rows = raw.get("data", [])

# Conversion en DataFrame
df = pd.DataFrame(rows)

# Gestion du cas vide
if df.empty:
    df = pd.DataFrame(columns=[
        "id",
        "user_id",
        "book_id",
        "loan_date",
        "return_date",
        "status"
    ])

# Nettoyage des données
df = df.dropna(subset=["user_id", "book_id"], how="any")

# Conversion des types
df["user_id"] = df["user_id"].astype(int)
df["book_id"] = df["book_id"].astype(int)

# Export CSV nettoyé
df.to_csv("dvc-pipeline/data/loans_clean.csv", index=False)

print("Preprocessing completed")
print(df.head())