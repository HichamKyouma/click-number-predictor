import json
import pickle as pkl

mapping_path = "artefacts/district_mapping.json"
scaler_path = "artefacts/scaler.pkl"
model_path = "models/click_predictor_xgb.pkl"


with open(mapping_path) as f:
    district_mapping = json.load(f)

with open(scaler_path, "rb") as f:
    MinMaxScaler = pkl.load(f)

with open(model_path, "rb") as f:
    model_xgb = pkl.load(f)
