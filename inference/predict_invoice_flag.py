from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "Models" / "predict_freight_model.pkl"

def load_model():
    model = joblib.load(MODEL_PATH)
    return model

def predict_freight_cost(input_data):
    """
    predict freight cost for new vendor invoices.

    Parameters

    input_data :dict

    Returns

    pd.DataFrame with predicted freight cost

    """
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Freight'] = model.predict(input_df).round()
    return input_df
if __name__ == "__main__":
    sample_data = {
    "Dollars": [18500, 9000, 3000, 200]
}
    prediction = predict_freight_cost(sample_data)
    print(prediction)
