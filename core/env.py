from functools import lru_cache
from pathlib import Path
from decouple import config as _config, Config, RepositoryEnv

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR.parent
ENV_FILE_PATH = PROJECT_DIR / ".env"


@lru_cache()
def get_config():
    if ENV_FILE_PATH.exists():
        return Config(RepositoryEnv(str(ENV_FILE_PATH)))
    return _config


config = get_config()
