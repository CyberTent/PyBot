from lib import *


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))

        print(f'Bot worked in {len(self.bot.guilds)} servers:')
        server_number = 1
        for server_name in self.bot.guilds:
            print(f'{server_number} | {server_name}')
            server_number += 1

        for guild in self.bot.guilds:
            print(len(guild.members))
            for member in guild.members:
                print(member, member.id, member.guild)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member, member.id, member.guild.id)

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message)


def setup(bot):
    print('info loaded')
    bot.add_cog(ServerInfo(bot))
