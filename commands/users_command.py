from lib import *


class UsersCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *,  avamember: discord.Member = None):
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)


def setup(bot):
    print('users_command loaded')
    bot.add_cog(UsersCommand(bot))
