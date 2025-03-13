import os
import pickle
import joblib
import uvicorn
import pandas as pd

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()


with open("getaround1_pipeline.pkl", "rb") as file:
    preprocessor = pickle.load(file)

model = joblib.load("getaround1_model.pkl")


class InputData(BaseModel):
    input: list


# -----------------------------------------------------------------------------

@app.post("/predict")
async def predict(data: InputData):
    try:
        input_data = data.input
        input_features = [
            "model_key",
            "mileage",
            "engine_power",
            "fuel",
            "paint_color",
            "car_type",
            "private_parking_available",
            "has_gps",
            "has_air_conditioning",
            "automatic_car",
            "has_getaround_connect",
            "has_speed_regulator",
            "winter_tires",
        ]
        input_df = pd.DataFrame(input_data, columns=input_features)
        preprocessed_data = preprocessor.transform(input_df)
        prediction = model.predict(preprocessed_data)
        return {"predict_price": f"{prediction[0]:.2f} euros"}
    except Exception as e:
        print(str(e))
        raise HTTPException(
            status_code=500,
            detail="Error getaround_api. vérifier le nombre de paramètres et leurs noms",
        )


# -----------------------------------------------------------------------------
@app.get("/docs")
async def get_docs():
    return {"docs_url": "/docs"}


# -----------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Documentation API Getaround</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    line-height: 1.6;
                }
                h1, h2 {
                    color: #333;
                }
                code {
                    background: #f4f4f4;
                    padding: 5px;
                    border-radius: 5px;
                    display: block;
                    white-space: pre-wrap;
                }
                .container {
                    max-width: 800px;
                    margin: auto;
                }
                .endpoint {
                    background: #eef;
                    padding: 10px;
                    border-left: 5px solid #36c;
                    margin-bottom: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Getaround API - Documentation</h1>
                <p>Cette API permet d'obtenir des propositions de prix pour la location de voitures.</p>

                <h2>Endpoints</h2>
                <div class="endpoint">
                    <strong>/predict</strong> : Permet d'obtenir des propositions de prix.
                </div>
                <div class="endpoint">
                    <strong>/docs</strong> : Permet de tester l'API en ligne.
                </div>

                <h2>Jeu de données de test</h2>
                <code>["Renault", "90000", "115", "diesel", "white", "suv", true, true, false, false, true, true, false]</code>

                <h2>Paramètres de l'API</h2>
                <ul>
                    <li><strong>model_key</strong> : Modèle de la voiture</li>
                    <li><strong>mileage</strong> : Kilométrage</li>
                    <li><strong>engine_power</strong> : Puissance du moteur</li>
                    <li><strong>fuel</strong> : Type de carburant</li>
                    <li><strong>paint_color</strong> : Couleur de la peinture</li>
                    <li><strong>car_type</strong> : Type de voiture</li>
                    <li><strong>private_parking_available</strong> : Parking privé disponible (true/false)</li>
                    <li><strong>has_gps</strong> : GPS intégré (true/false)</li>
                    <li><strong>has_air_conditioning</strong> : Climatisation (true/false)</li>
                    <li><strong>automatic_car</strong> : Boîte automatique (true/false)</li>
                    <li><strong>has_getaround_connect</strong> : Getaround Connect disponible (true/false)</li>
                    <li><strong>has_speed_regulator</strong> : Régulateur de vitesse (true/false)</li>
                    <li><strong>winter_tires</strong> : Pneus hiver (true/false)</li>
                </ul>

                <h2>Exemple d'utilisation en ligne de commande</h2>
                <code>
        curl -i -H "Content-Type: application/json" -X POST -d '{"input": [["Renault", "90000", "115", "diesel", "white", "suv", true, true, false, false, true, true, false]]}' https://sg1961-get-around-api.hf.space/predict
                </code>
            </div>
        </body>
        </html>
    """
    return html_content
