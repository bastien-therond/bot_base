from discord.ext import commands

class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.money = 0
        self.banque = 0

    @commands.command(name='depot')
    async def depot_money(self, ctx, arg):
        if self.money <= int(arg):
            await ctx.send(f"Pas assez d'argent\nArgent actuel = {self.money}")
        else:
            self.money = self.money+int(arg)
            await ctx.send(f"Virement éffectuée\nArgent actuel = {self.money}")

    #Pour les test !!!!!
    @commands.command(name='ajout')
    async def ajout(self, ctx, arg):
        self.money = self.money + int(arg)
        await ctx.send(f"Argent mise à jour\nArgent actuel = {self.money}")

    @commands.command(name='banque')
    async def banque(self, ctx):
        await ctx.send(f"Argent liquide = {self.money}\nArgent en banque = {self.banque}")

    @commands.Cog.listener(name='on_ready')
    async def on_ready(self):
        print('Cog Economy ready')



def setup(bot):
    return bot.add_cog(Economy(bot))