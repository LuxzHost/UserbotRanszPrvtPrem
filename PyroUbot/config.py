import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7763380474").split()))

API_ID = int(os.getenv("API_ID", "28036572"))

API_HASH = os.getenv("API_HASH", "c8e6d2a215b723989eb1419ea921db82")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8051785072:AAEi630rPp5phqTRA2Rgdhq5tFFkjotP9DI")

OWNER_ID = int(os.getenv("OWNER_ID", "7763380474"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002562922417").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Ipanndongok:Ipanndongok@ipanndongok.bg7xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002562922417"))
