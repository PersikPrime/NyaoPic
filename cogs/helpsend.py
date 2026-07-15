import disnake
from disnake.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="help", description="Get help with the bot commands")
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(
            title="Help Commands",
            description="Here are the available commands for the bot:",
            color=0xFFB6C1
        )
        embed.add_field(name="/neko", value="Get a random neko art ✨", inline=False)
        embed.add_field(name="/kitsune", value="Get a random kitsune art ✨", inline=False)
        embed.add_field(name="/waifu", value="Get a random waifu art ✨", inline=False)
        
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(HelpCommands(bot))