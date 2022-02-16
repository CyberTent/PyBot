from lib import *
import settings.token as token

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

extensions = [
    'games.minesweeper',
    'commands.users_command',
    'server_info.info'
]

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


print("---fine---")
client.run(token.TOKEN)
