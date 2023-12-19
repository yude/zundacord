import discord
from discord.ext import commands
from mylib.constant import EXTENSIONS, TOKEN


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="/",
            intents=discord.Intents.all(),
        )

    async def setup_hook(self):
        for extention in EXTENSIONS:
            await self.load_extension(extention)
        await self.tree.sync()


if __name__ == "__main__":
    bot = MyBot()
    bot.run(token=TOKEN)
