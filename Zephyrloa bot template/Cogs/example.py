import discord
from discord import app_commands
from discord.ext import commands

class exampleclass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        #↑ もし特定のGuildで使用する場合は()内に、guild=discord.Object(ギルドID)を打つことで使用できます
        print("ready")

    @app_commands.command(name = "example", description = "test command")
    #@app_commands.checks.has_permissions(administrator=True)
    #↑Adominのみ使用にする場合は有効にしてください。
    async def exampletest(self, interaction):
        await interaction.response.send_message("zephyrloa")
            
async def setup(bot: commands.Bot):
    await bot.add_cog(exampleclass(bot))
