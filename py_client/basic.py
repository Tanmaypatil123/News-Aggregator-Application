# import requests

# endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint)
# print(get_response.json())

from pathlib import Path
from datetime import timedelta
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent 

print(str(BASE_DIR) + r"\news_app\.env")