from pydantic import BaseSettings
from dotenv import load_dotenv

# from dotenv import find_dotenv

load_dotenv()


class GlobalConfig(BaseSettings):
    # DB_HOST: str = "http://dynamodb:8000"
    # ENVIRONMENT: str = "test"
    AWS_REGION: str = "eu-north-1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

        # env_file = find_dotenv(".env")


config = GlobalConfig()
