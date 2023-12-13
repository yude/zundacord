import os
from dotenv import load_dotenv

load_dotenv()

EXTENTIONS = [
    "cogs.zunda",
]
TOKEN = os.environ["TOKEN"]