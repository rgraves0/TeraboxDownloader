from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 8802706)  # api id
API_HASH = environ.get("API_HASH", "97546900397a98f481bfb8252b1ac4f4")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "7525934578:AAELTa7n9hD5b6gruY_Pm-rT7YCLwxV5Dao")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "localhost")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 12345)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "q8vcRgGfoZgwKT6irvJ6AixPs1lFZdW8"
)  # redis password


ADMINS = [1281749717]
OWNER_ID = 1281749717  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002279229538  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1002279229538
DUMP_CHANNEL = -1002279229538


# Config
COOKIE = environ.get("COOKIE", "")
