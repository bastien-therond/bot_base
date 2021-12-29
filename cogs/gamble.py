from discord.ext import commands
import random

class Gamble(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_ready')
    async def on_ready(self):
        print("Cog Gamble ready")

    @commands.command(name='coinflip')
    async def coinflip(self, ctx):
        await ctx.send('zet')
        pass

    @commands.command(name='randomInt')
    async def randomNumber(self, ctx, arg):
        chiffre = random.randint(0, int(arg))
        await ctx.send(f'Le nombre sera de {chiffre}')


def setup(bot):
    return bot.add_cog(Gamble(bot))