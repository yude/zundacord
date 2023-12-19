import os
from dotenv import load_dotenv

load_dotenv()

EXTENSIONS = [
    "cogs.zunda",
]
TOKEN = os.environ["TOKEN"]
