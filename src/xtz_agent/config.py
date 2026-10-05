from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="XTZ_", env_file=".env", extra="ignore")
    llm_base_url: str | None = None
    llm_api_key: str | None = None
    llm_model: str | None = None
    knowledge_dir: Path = Path("knowledge")
    twin_db: Path = Path(".data/xtz_twin.sqlite3")
    log_level: str = "INFO"
    allow_remote_vision: bool = False

settings = Settings()
