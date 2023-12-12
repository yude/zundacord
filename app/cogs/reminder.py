from discord.ext import commands, tasks
from mylib.constant import REMINDER_CHANNEL_ID


class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminder.start()

    @tasks.loop(seconds=5.0, count=5)
    async def reminder(self):
        channel = self.bot.get_channel(REMINDER_CHANNEL_ID)
        await channel.send("リマインダー！")

    @reminder.before_loop
    async def before_reminder(self):
        await self.bot.wait_until_ready()


async def setup(bot):
    await bot.add_cog(Reminder(bot))
