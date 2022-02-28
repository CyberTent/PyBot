import discord

from discord.ext import commands

from datetime import datetime
from settings.bot_log import *


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))
        guild = self.bot.get_guild(id=guild_id)

        print(f'Bot worked in {len(self.bot.guilds)} servers:')
        server_number = 1
        member_count = 1

        id_all_channels = ''
        id_all_members = ''
        id_server = ''
        id_log = ''

        for server_name in self.bot.guilds:
            category_name = str(server_name).lower()

            if category_name.lower() not in [str(category).lower() for category in guild.categories]:
                await guild.create_category(category_name)
                cat = discord.utils.get(guild.categories, name=category_name)

                channel_name = 'channels'
                channel_new_channels = await guild.create_text_channel(channel_name, category=cat)
                id_all_channels = channel_new_channels.id
                await channel_new_channels.send(f'{id_all_channels}')
                '''channel_name = 'members'
                channel_new_members = await guild.create_text_channel(channel_name, category=cat)
                id_all_members = channel_new_members.id
                await channel_new_members.send(f'{id_all_members}')
                channel_name = 'server_info'
                channel_new_server = await guild.create_text_channel(channel_name, category=cat)
                id_server = channel_new_server.id
                await channel_new_server.send(f'{id_server}')
                channel_name = '<log>'
                channel_new_log = await guild.create_text_channel(channel_name, category=cat)
                id_log = channel_new_log.id
                await channel_new_log.send(f'{id_log}')'''

            print(f'{server_number} | {server_name} | {server_name.id} | {len(server_name.members)}')

            if len(server_name.categories) != 0:
                for channel in server_name.text_channels:
                    if channel.category_id is None:
                        print(f'Текст: {channel} || {channel.id}')
                for channel in server_name.voice_channels:
                    if channel.category_id is None:
                        print(f'Голос: {channel} || {channel.id}')
            if len(server_name.categories) != 0:
                '''print(server_name.categories)
                print(server_name.text_channels)
                print(server_name.voice_channels)'''
                for category in server_name.categories:
                    print(f'Категория: {category} || {category.id}')
                    for channel in category.text_channels:
                        print(f'\tТекст: {channel} || {channel.id}')
                    for channel in category.voice_channels:
                        print(f'\tГолос: {channel} || {channel.id}')
            else:
                for channel in server_name.text_channels:
                    print(f'Текст: {channel} || {channel.id}')
                for channel in server_name.voice_channels:
                    print(f'Голос: {channel} || {channel.id}')

            for member in server_name.members:
                print(f'\t{member_count} || {member.nick} || {member.name} || '
                      f'{member.discriminator} || {member.id} || {member.bot} || ')
                member_count += 1
            member_count = 1
            server_number += 1

            await self.bot.get_channel(id_all_channels).purge(limit=100)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # print(member, member.id, member.guild.id)
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        channel_id = self.bot.get_channel(id=int(message.channel.id))
        link = await channel_id.create_invite(max_age=120)
        channel = self.bot.get_channel(id=messages_channel)

        '''msg = f'{message.guild}: {message.created_at} | {message.channel} | {message.author}|' \
              f' {message.author.id} | {message.author.bot}:\n```{message.content}```'''

        if message.channel.id != messages_channel and message.author.bot is not True:
            embed = discord.Embed(title="Message log", colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            embed.add_field(name="Server", value=f'**name:** {message.guild}\n**id:** {message.guild.id}', inline=False)
            embed.add_field(name="Channel", value=f'**name:** {message.channel}\n**id:** {message.channel.id}')
            embed.add_field(name="Message content", value=message.content, inline=False)
            embed.set_footer(text=f'Bot: {message.author.bot}',
                             icon_url='https://cdn.discordapp.com/emojis/750830349348634625.gif')
            embed.add_field(name="Link", value=link, inline=False)
            await channel.send(embed=embed)


def setup(bot):
    print('info loaded')
    bot.add_cog(ServerInfo(bot))
