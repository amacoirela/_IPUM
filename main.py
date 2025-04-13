import argparse
import os
from dotenv import load_dotenv
import yaml
from settings import Settings


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

    # Wczytaj odszyfrowany plik YAML
    yaml_file = f"secrets-{environment}.yaml"
    if os.path.exists(yaml_file):
        with open(yaml_file, "r") as file:
            config = yaml.safe_load(file)
            for key, value in config.items():
                os.environ[key] = str(value)
    else:
        raise FileNotFoundError(f"Plik {yaml_file} nie istnieje")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from the specified .env and YAML files."
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
    print("SECRET: ", settings.SECRET_KEY)
