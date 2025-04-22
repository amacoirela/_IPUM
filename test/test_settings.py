# test_settings.py
import os
from settings import Settings
from dotenv import load_dotenv


def test_settings_load_correctly():
    # Załaduj zmienne środowiskowe z pliku .env.test
    load_dotenv(dotenv_path="./IPUM/.env.test")

    # Utwórz instancję Settings
    settings = Settings()

    # Sprawdź, czy wartości są poprawnie załadowane
    assert settings.ENVIRONMENT == os.getenv("ENVIRONMENT")
    assert settings.APP_NAME == os.getenv("APP_NAME")