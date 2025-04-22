# training.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


def load_data():
    """
    Ładuje zbiór danych Iris i zwraca dane oraz etykiety.
    """
    data = load_iris()
    X, y = data.data, data.target
    return X, y


def train_model(X, y):
    """
    Trenuje model klasyfikacyjny RandomForest na podanych danych.
    Zwraca wytrenowany model.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    return model


def save_model(model, file_path="model.joblib"):
    """
    Zapisuje wytrenowany model do pliku.
    """
    joblib.dump(model, file_path)
    print(f"Model saved to {file_path}")


if __name__ == "__main__":
    # Przykładowe użycie
    X, y = load_data()
    model = train_model(X, y)
    save_model(model)