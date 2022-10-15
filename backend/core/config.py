import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.')/'.env'
env_path = os.path.abspath(env_path)
load_dotenv(dotenv_path=env_path)

print(f'\n\nenv_path: {env_path}\n\n')

class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    # default postgres host is set to localhost
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
    # default postgres port is 5432
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    print(DATABASE_URL)




settings = Settings()
