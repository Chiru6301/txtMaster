import os

API_ID = API_ID = 28817205

API_HASH = os.environ.get("API_HASH", "f319d02866bf7b83e4de31002f6ba8a3")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8142665720:AAGlRGV0yTCAKtDVfruzOhu0vrtXK2F1l2E")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7935947598))

LOG = -1002468082777

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7935947598").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
