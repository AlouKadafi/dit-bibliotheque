import json
import pickle
from pathlib import Path

# Création dossier metrics
Path("metrics").mkdir(exist_ok=True)

# Chargement modèle
with open("dvc-pipeline/models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Métriques simples
metrics = {
    "total_books": len(model["book_popularity"]),
    "status": "success"
}

# Sauvegarde métriques
with open("metrics/metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("Evaluation completed")
print(metrics)