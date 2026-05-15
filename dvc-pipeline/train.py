import pandas as pd
import pickle
from pathlib import Path

# Création du dossier models
Path("dvc-pipeline/models").mkdir(parents=True, exist_ok=True)

# Chargement des données
df = pd.read_csv("dvc-pipeline/data/loans_clean.csv")

# Modèle très simple basé sur popularité des livres
book_counts = df["book_id"].value_counts().to_dict()

model = {
    "book_popularity": book_counts
}

# Sauvegarde du modèle
with open("dvc-pipeline/models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Training completed")
print(model)