import re
import aiohttp
from discord.ext import commands

class NudeityDetector (commands.Bot):
    def __init__(self,command_prefix,**options):
        super().__init__(command_prefix,**options)
        self.DEEPAI_KEY = "##"
        self.DEEPAI_API_URL="https://api.deepai.org/a"

    async def detect_nudity(self,link):
        async with aiohttp.ClientSession()as session:
            async with session.post(self.DEEPAI_API_URL, data={'image':link},headers={'api-key':self.DEEPAI_KEY})as response:
                data=await response.json()
                print(data)

    async def on_ready(self):
        print("ready")

    async def on_message(self, message):
        URL_REGEX = "http[s]?://(?;[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|[!*(),]|(?:%[0-9a-fA-F]))+"
        urls =re.findall(URL_REGEX,message.content)
        links=[link.strip("<>")for link in urls] + [file.url for file in message.attachment]

        for link in links:
            await self.detect_nudity(link)

bot=NudeityDetector(command_prefix="m.")
bot.run("##")
