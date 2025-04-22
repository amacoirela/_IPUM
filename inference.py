# inference.py
import joblib
import numpy as np


def load_model(file_path="model.joblib"):
    """
    Ładuje wytrenowany model z pliku.
    """
    model = joblib.load(file_path)
    print(f"Model loaded from {file_path}")
    return model


def predict(model, input_data):
    """
    Wykonuje predykcję na podstawie danych wejściowych.
    Zwraca przewidywaną klasę jako string.
    """
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return str(prediction[0])


if __name__ == "__main__":
    # Przykładowe użycie
    model = load_model()
    sample_input = [5.1, 3.5, 1.4, 0.2]  # Przykładowe dane wejściowe
    result = predict(model, sample_input)
    print(f"Predicted class: {result}")