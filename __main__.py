from app.config.constants import TOKEN
from app.libs.bot import bot


# Init the bot with the token
def run():
    bot.run(TOKEN)


if __name__ == "__main__":
    run()
