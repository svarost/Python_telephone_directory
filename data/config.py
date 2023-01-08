import os

from dotenv import load_dotenv

load_dotenv()

# Забераем токен нашего бота (прописать в файле ".env")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

