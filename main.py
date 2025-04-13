import argparse
from settings import Settings
import os
from dotenv import load_dotenv


def export_envs(environment: str = "dev") -> None:
    # Mapowanie środowisk na pliki .env
    env_files = {
        "dev": ".env.dev",
        "test": ".env.test",
        "prod": ".env.prod",
    }

    # Wybierz odpowiedni plik .env
    env_file = env_files.get(environment)
    if not env_file:
        raise ValueError(f"Nieznane środowisko: {environment}")

    # Sprawdź, czy plik istnieje
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Plik {env_file} nie istnieje")

    # Załaduj zmienne środowiskowe z pliku
    load_dotenv(env_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
