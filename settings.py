from dotenv import load_dotenv
import os

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_FULL_URL = os.getenv("REDIS_FULL_URL")
ELASTIC_HOST = os.getenv("ELASTIC_HOST")
ELASTIC_PORT = os.getenv("ELASTIC_PORT")
LOG_FILE = os.getenv("LOG_FILE")
FILE_EXTENSION = os.getenv("FILE_EXTENSION")
