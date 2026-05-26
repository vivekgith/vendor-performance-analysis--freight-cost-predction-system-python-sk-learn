from modeling_evaluation import train_random_forest, evaluate_classifier
from data_preprocessing import load_invoice_data, apply_labels, split_data, scale_features
import joblib

FEATURES = [
    "invoice_quantity",
    "invoice_dollars", 
    "Freight", 
    "total_item_quantity", 
    "total_item_dollars",

]
TARGET = "flag_invoice"


def main():
    df = load_invoice_data() #load data
    df = apply_labels(df)
    X_train, X_test, y_train, y_test = split_data(df, FEATURES, TARGET)#prepare data
    X_train_scaled, X_test_scaled = scale_features(
        X_train, X_test, 'models/scaler.pkl'
    )

    #conn = sqlite3.connect("/Users/vivekrajverma/Data_Analysis_Large_Project/freight_cost_prediction/inventory.db")

    #query = "SELECT * FROM vendor_invoice"

    #df = load_invoice_data(query, conn)

   # df = apply_labels(df)

   # train and evaluate models
    grid_search = train_random_forest(X_train_scaled, y_train)

    evaluate_classifier(
        grid_search.best_estimator_,
        X_test_scaled,
        y_test,
        "Random Forest Classifier"
    )

    # Save model
    joblib.dump(
        grid_search.best_estimator_,
        'models/predict_flag_invoice.pkl'
    )
if __name__ == "__main__":
    main()
