import json

bot_config = json.load(open("./app/config/bot_setup.json","r"))

TOKEN = bot_config["token"]
LOG_CHANNEL = bot_config["logger_channel"]
BOT_PREFIX = bot_config["bot_prefix"]