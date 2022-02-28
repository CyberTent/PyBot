import discord

from discord.ext import commands
from settings.bot_log import *


class UsersCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Получение аватарки пользователя
    @commands.command()
    async def avatar(self, ctx, *,  member: discord.Member = None):
        await ctx.send(member.avatar_url)

    # Создание категорий/каналов
    '''@commands.command()
    async def new(self, ctx, arg1, arg2):
        guild = self.bot.get_guild(id=guild_id)
        if arg1 == "channel":
            if arg2.lower() not in [str(channel) for channel in guild.text_channels]:
                cat = discord.utils.get(ctx.guild.categories, name="TEST")
                await ctx.guild.create_text_channel(arg2, category=cat)

        elif arg1 == "category":
            if arg2.lower() not in [str(category) for category in guild.categories]:
                await ctx.guild.create_category(arg2)'''


def setup(bot):
    print('users_command loaded')
    bot.add_cog(UsersCommand(bot))
