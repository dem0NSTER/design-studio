import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')


@dataclass
class Config:
    DB_HOST: str
    DB_PORT: str
    DB_PASS: str
    DB_USER: str
    DB_NAME: str

    @property
    def async_link_to_connect(self):
        # postgresql+asyncpg://user:pass@hostname/dbname
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


db_settings = Config(DB_HOST, DB_PORT, DB_PASS, DB_USER, DB_NAME)


if __name__ == '__main__':
    print(db_settings.async_link_to_connect)
