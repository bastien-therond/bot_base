from discord.ext import commands
import sqlite3
from BDD.command_bdd import command_bdd

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.id = 0
        self.con = sqlite3.connect("BDD/bot_base.db")
        self.bdd = command_bdd()

    @commands.Cog.listener(name='on_ready')
    async def on_ready(self):
        print("Cog Main ready")

    @commands.command(name="register")
    async def register(self, ctx):
        for row in self.bdd.getAllUser:
            print(row)
        pass

def setup(bot):
    return bot.add_cog(Cog(bot))