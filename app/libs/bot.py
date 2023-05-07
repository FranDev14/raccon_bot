import discord
from discord.ext.commands import Bot, when_mentioned_or
from app.config.constants import BOT_PREFIX
from app.utils.logger import DiscordHandler
import logging


# Create the bot with the needed intents, you can add more if you want it
logger = logging.getLogger(__name__)
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

# Init the bot with the prefix configured in the config file
bot = Bot(command_prefix=when_mentioned_or(BOT_PREFIX),intents=intents)

logger.addHandler(DiscordHandler(bot))
logger.setLevel(logging.INFO)

bot.log = logger

# Extension system for the bot
bot.load_extension("app.modules.general")