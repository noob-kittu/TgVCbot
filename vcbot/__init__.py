import os
import logging

from telethon import TelegramClient
from telethon.sessions import StringSession

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

API_ID = os.environ.get("API_ID", default=None)
API_HASH = os.environ.get("API_HASH", default=None)
STRING = os.environ.get("STRING", default=None)


app = TelegramClient(StringSession(STRING), api_id=API_ID, api_hash=API_HASH)




