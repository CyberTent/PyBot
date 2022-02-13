from lib import *
import settings.token as token

client = commands.Bot(command_prefix='.')

extensions = [
    'games.minesweeper',
    'commands.users_command'
]

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


print("bot.py started")
client.run(token.TOKEN)
