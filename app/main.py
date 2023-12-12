import discord
from discord.ext import commands
from mylib.constant import EXTENTIONS, TOKEN


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="/",
            intents=discord.Intents.all(),
        )

    async def setup_hook(self):
        for extention in EXTENTIONS:
            await self.load_extension(extention)


if __name__ == "__main__":
    bot = MyBot()
    bot.run(token=TOKEN)
