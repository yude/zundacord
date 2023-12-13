from discord.ext import commands
import discord
import requests
import uuid
import json
import asyncio

class Zunda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def zunda(self, ctx, arg):
        this_uuid = uuid.uuid1(node=None, clock_seq=None)

        res_parameter = requests.post(
            "http://voicevox:50021/audio_query",
            params = (
                ('text', arg),
                ('speaker', 1),
            )
        )

        res_voice = requests.post(
            "http://voicevox:50021/synthesis",
            headers = {'Content-Type': 'application/json'},
            params = (
                ('text', arg),
                ('speaker', 1),
            ),
            data = json.dumps(res_parameter.json())
        )

        with open(f"waves/{str(this_uuid)}.wav", mode="wb") as f:
            f.write(res_voice.content)

        if ctx.author.voice is None:
            with open(file=f"waves/{str(this_uuid)}.wav", mode="rb") as f:
                await ctx.send(
                    content = "どうぞ〜〜〜",
                    file = discord.File(f),
                    silent = True,
                )
        else:
            v_client = await ctx.author.voice.channel.connect()
            await asyncio.sleep(0.8)
            source = discord.FFmpegPCMAudio(f"waves/{str(this_uuid)}.wav")
            v_client.play(source)
            await v_client.disconnect(force=True)
            v_client.cleanup()
        


async def setup(bot):
    await bot.add_cog(Zunda(bot))
