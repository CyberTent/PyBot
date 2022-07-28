import discord

from discord.ext import commands


class UsersCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Получение аватарки пользователя
    @commands.command()
    async def avatar(self, ctx, *,  member: discord.Member = None):
        await ctx.send(member.avatar_url)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Команды сервера", colour=0x00FF00)
        embed.set_author(name='Информатор',
                         icon_url='https://cspromogame.ru//storage/upload_images/avatars/2038.jpg')
        embed.add_field(name='Пользовательские',
                        value='.avatar\n'
                              '.help\n', inline=False)
        embed.add_field(name='Продвинутые',
                        value='.say\n'
                              '.clear\n', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    print('users_command loaded')
    bot.add_cog(UsersCommand(bot))
