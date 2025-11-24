

from os import environ

API_ID = int(environ.get("API_ID", "29731917"))
API_HASH = environ.get("API_HASH", "d0b73a75f2d12cae5b04c21044ff0148")
BOT_TOKEN = environ.get("BOT_TOKEN", "7698119810:AAGh5Q7Hwa8-a09XUSuuyZPb2mxzsXp4NwY")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/chaiabah")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/chaiabah")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "8050673236").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "8050673236"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")






