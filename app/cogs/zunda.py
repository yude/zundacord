from discord.ext import commands
from discord import app_commands
import discord

import requests
import uuid
import json

class Zunda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="zunda", description="ずんだを生成します")
    @app_commands.describe(text="ずんだの内容")
    async def zunda(self, interaction: discord.Interaction, text: str):
        this_uuid = uuid.uuid1(node=None, clock_seq=None)

        res_parameter = requests.post(
            "http://voicevox:50021/audio_query",
            params = (
                ('text', text),
                ('speaker', 1),
            )
        )

        res_voice = requests.post(
            "http://voicevox:50021/synthesis",
            headers = {'Content-Type': 'application/json'},
            params = (
                ('text', text),
                ('speaker', 1),
            ),
            data = json.dumps(res_parameter.json())
        )

        with open(f"waves/{str(this_uuid)}.wav", mode="wb") as f:
            f.write(res_voice.content)

        with open(file=f"waves/{str(this_uuid)}.wav", mode="rb") as f:
            await interaction.response.send_message(
                content = "どうぞなのだ",
                file = discord.File(f),
                silent = True,
            )


async def setup(bot):
    await bot.add_cog(Zunda(bot))
