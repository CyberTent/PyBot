import discord

from discord.ext import commands


from datetime import datetime
from settings.bot_log import *


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(view_audit_log=True)
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)

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
                      f'{member.discriminator} || {member.id} || {member.bot} || ')
                member_count += 1
            member_count = 1
            server_number += 1

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member, member.id, member.guild.id)

    @commands.Cog.listener()
    async def on_message(self, message):
        embed = discord.Embed(title="Message log", colour=0x87CEEB, timestamp=datetime.utcnow())
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="Server", value=message.guild, inline=False)
        embed.add_field(name="Channel", value=message.channel, inline=False)
        embed.add_field(name="Message content", value=message.content, inline=False)
        embed.set_footer(text=f'Bot:{message.author.bot}',
                         icon_url='https://cdn.discordapp.com/emojis/750830349348634625.gif?size=60&quality=lossless')

        channel_id = self.bot.get_channel(id=int(message.channel.id))
        channel = self.bot.get_channel(id=messages_channel)
        msg = f'{message.guild}: {message.created_at} | {message.channel} | {message.author}|' \
              f' {message.author.id} | {message.author.bot}:\n```{message.content}```'

        if message.channel.id != messages_channel:
            if message.author.bot and len(message.content) != 0:
                if message.guild.id != guild_id:
                    link = await channel_id.create_invite(max_age=120)
                    embed.add_field(name="Link", value=link, inline=False)
                    print(link)
                await channel.send(embed=embed)
            elif message.author.bot is not True and len(message.content) != 0:
                if message.guild.id != guild_id:
                    link = await channel_id.create_invite(max_age=120)
                    embed.add_field(name="Link", value=link, inline=False)
                    print(link)
                await channel.send(embed=embed)
            else:
                if message.guild.id != guild_id:
                    link = await channel_id.create_invite(max_age=120)
                    embed.add_field(name="Link", value=link, inline=False)
                    print(link)
                await channel.send(embed=embed)


def setup(bot):
    print('info loaded')
    bot.add_cog(ServerInfo(bot))
