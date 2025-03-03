import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("final_labeled_dataset.csv")

# Drop irrelevant or NaN columns
df = df.drop(columns=['missing_info_y'], errors='ignore')

# Define features and target
X = df.drop(columns=['storage_strategy'])  # Features
y = df['storage_strategy']  # Target

# Replace infinity values with NaN
X.replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop or replace NaN values with mean
X.fillna(X.mean(), inplace=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Decision Tree Classifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Evaluate model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Cross-validation
cv_scores = cross_val_score(clf, X, y, cv=5)
print(f"Cross-validation Accuracy: {np.mean(cv_scores):.4f} ± {np.std(cv_scores):.4f}")

# Feature importance
plt.figure(figsize=(10, 5))
plt.barh(X.columns, clf.feature_importances_)
plt.xlabel("Feature Importance")
plt.ylabel("Features")
plt.title("Feature Importance in Decision Tree")
plt.show()

# Visualizing decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=["Strategy 0", "Strategy 1"], filled=True)
plt.show()

# ✅ Save the trained model correctly
joblib.dump(clf, "saved_model.pkl")
print("Model saved successfully!")
