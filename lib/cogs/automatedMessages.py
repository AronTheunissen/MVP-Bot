from discord.ext.commands import Cog

class AutomatedMessages(Cog):
    def __init__(self, bot):
        self.bot = bot


    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Sup")
        print("Online!")

async def setup(bot):
    await bot.add_cog(AutomatedMessages(bot))