import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

# Load trained model
clf = joblib.load("saved_model.pkl")

# Load unseen test dataset
df_test = pd.read_csv("unseen_data.csv")

# Ensure only the correct feature columns are selected
expected_features = clf.feature_names_in_
X_test = df_test.reindex(columns=expected_features, fill_value=0)  # Fill missing columns with 0

# Predict
predictions = clf.predict(X_test)

# Print accuracy
print(f"Accuracy on synthetic unseen data: {accuracy_score(df_test['storage_strategy'], predictions):.4f}")
print("Classification Report:\n", classification_report(df_test['storage_strategy'], predictions))
