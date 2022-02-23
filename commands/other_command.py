import discord
from discord.ext import commands

from datetime import datetime


class OtherCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Озвучка сообщений через бота
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, arg1):
        try:
            # await ctx.channel.purge(limit=1)
            my_channel = self.bot.get_channel(id=int(arg1))
            await my_channel.send(ctx.message.content.replace('.say', '').replace(f'{arg1}', ''), tts=True)
        except:
            embed = discord.Embed(title="Error message", colour=0xFF0000, timestamp=datetime.utcnow())
            embed.set_author(name='Информатор',
                             icon_url='https://cspromogame.ru//storage/upload_images/avatars/2038.jpg')
            embed.add_field(name="Причины возникновения ошибок",
                            value='**1.** Неверная структура комманды\n'
                                  '**2.** Указанный id несуществует\n'
                                  '**3.** Нет доступа к указанному чату', inline=False)
            embed.add_field(name="Структура комманды",
                            value='```.say [id канала] [сообщение]```', inline=False)
            await ctx.send(embed=embed)

    # Очистка чата
    @commands.command(pass_context=True)
    @commands.has_permissions(view_audit_log=True)
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)


def setup(bot):
    print('other_command loaded')
    bot.add_cog(OtherCommand(bot))
