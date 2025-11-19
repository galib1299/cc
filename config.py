import os

API_ID = 26375665

API_HASH = os.environ.get("API_HASH", "568839157ce65f4d3a91647f022b6737")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8249505758:AAEkxJvq-sRLurMGqcaogbMgJ_MXssilQ7I")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "6834250190"))

LOG = int(os.environ.get("LOG", "1"))

PORT = os.environ.get("PORT", "8080")

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6834250190").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
