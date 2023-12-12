from discord.ext import commands
import discord
import requests
import uuid
import json
import wave

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

        wf = wave.open(str(this_uuid)+'.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(res_voice.content)
        wf.close()

        with open(file=str(this_uuid)+".wav", mode="rb") as file:
            await ctx.send("どうぞ〜〜〜", file=discord.File(file))
        

async def setup(bot):
    await bot.add_cog(Zunda(bot))
