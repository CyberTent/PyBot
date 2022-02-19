import discord

from discord.ext import commands


class OtherCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Озвучка сообщений через бота
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx):
        await ctx.channel.purge(limit=1)
        channel_id = int(ctx.message.content.split()[1])
        my_channel = self.bot.get_channel(id=channel_id)
        await my_channel.send(ctx.message.content.replace('.say', '').replace(f'{channel_id}', ''), tts=True)
        '''while True:
            await my_channel.send('https://boobzone.pro/uploads/posts/2022-01/1641190928_4-boobzone-pro-p-krasivie-muzhskie-chleni-porno-4.jpg')'''

    # Очистка чата
    @commands.command(pass_context=True)
    @commands.has_permissions(view_audit_log=True)
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)


def setup(bot):
    print('other_command loaded')
    bot.add_cog(OtherCommand(bot))