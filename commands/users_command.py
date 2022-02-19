import discord

from discord.ext import commands


class UsersCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Получение аватарки пользователя
    @commands.command()
    async def avatar(self, ctx, *,  member: discord.Member = None):
        await ctx.send(member.avatar_url)


def setup(bot):
    print('users_command loaded')
    bot.add_cog(UsersCommand(bot))
