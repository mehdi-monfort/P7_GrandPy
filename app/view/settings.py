import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.getenv("MAPS")
GEOCODE_BASE_URL = "https://geocode.search.hereapi.com/v1/geocode"
