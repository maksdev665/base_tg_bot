from typing import List
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, PostgresDsn, computed_field, field_validator


BASE_DIR = Path(__file__).resolve().parent.parent  # корень проекта

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",  # 👈 указываем абсолютный путь
        env_file_encoding='utf-8',
        extra='ignore'
    )

    # Bot settings
    bot_token: SecretStr
    admin_ids: List[int]

    # Database
    db_host: str = 'localhost'
    db_port: int = 5432
    db_name: str = 'bot_database'
    db_user: str = 'postgres'
    db_password: SecretStr = SecretStr('postgres')

    # Redis settings
    redis_host: str = 'localhost'
    redis_port: int = 6379

    @field_validator('admin_ids', mode='before')
    @classmethod
    def parse_admin_ids(cls, v):
        if isinstance(v, str):
            return [int(x.strip()) for x in v.split(',')]
        return v

    @computed_field
    @property
    def database_url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            username=self.db_user,
            password=self.db_password.get_secret_value(),
            host=self.db_host,
            port=self.db_port,
            path=self.db_name
        )
    
    @computed_field
    @property
    def redis_url(self) -> str:
        return f'redis://{self.redis_host}:{self.redis_port}'


settings = Settings()

