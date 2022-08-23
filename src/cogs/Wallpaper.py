import discord
from discord.ext import commands
import requests
import json
import random
import nekos
from bs4 import BeautifulSoup
import lxml
import validators
import topgg
import asyncio
with open('sfw_json/wallpaper.json', 'r') as f:
    src_wallpaper = json.load(f)

from itertools import cycle
async def god(cat):
       url = f"https://api.waifu.pics/sfw/{cat}"
       r = requests.get(url)
       link = json.loads(r.text)
       crtlink = link["url"]
       return crtlink
wall=cycle(["https://www.wallpaperflare.com/search?wallpaper=","https://www.peakpx.com/en/search?q=","https://www.wallpaperbetter.com/en/search?q="])
class Example(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("wallpaper is ready")

    @commands.command()
    @commands.guild_only()
    async def wallpaper(self,ctx, *,arg=""):
        if arg=="":
                 ppo=random.randint(0,1)
                 if ppo==0:
                       crtlink = (nekos.img("wallpaper"))
                       embed = discord.Embed(description =f"[Download]({crtlink})",colour=0x39138b)
                       embed.set_image(url=crtlink)
                       await ctx.reply(embed=embed,mention_author=False)

                 else:
                       crtlink = random.choice(src_wallpaper)
                       embed = discord.Embed(description =f"[Download]({crtlink})",colour=0x39138b)
                       embed.set_image(url=crtlink)
                       await ctx.reply(embed=embed,mention_author=False)
        else:
            name=arg.replace(" ","+")

            url=next(wall)+name
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'lxml')
            image_link = soup.find_all('img')

            a = str(image_link)
            a = a.split('"')
            b = []
            for r in range(0, len(a) - 1):
                if a[r] == "/>, <img alt=":
                    c = [a[r + 1]]
                    b = b + c
                if a[r] == " data-src=":
                    c = [a[r + 1]]
                    b = b + c
            rn = random.choice(range(0, len(b), 2))
            print(b[rn])
            crtlink = (b[rn + 1])
            embed = discord.Embed(title=arg, description=f"[{b[rn]}]({crtlink})",timestamp=(ctx.message.created_at),colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)    
            
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def waifu(self,ctx,n:int=1):
        a=ctx.message.author
        if n>11:
            n=10
        if n!=1 :
            if await self.client.topgg.get_user_vote(user_id =ctx.author.id):
                for i in range(n):
                    cat = "waifu"
                    crtlink=await god(cat)
                    embed = discord.Embed(colour=0x39138b)
                    embed.set_footer(text=f"{(a.name)} uWu ❣️ ",
                            icon_url=a.avatar_url)
                    embed.set_image(url=crtlink)
                    await ctx.send(embed=embed)
                    if (i % 2) == 0:
                        await asyncio.sleep(2)
            else:
                    embed = discord.Embed(description= "**[Vote Here](https://top.gg/bot/876139135507763280/vote)**\n\n<:upvote:893317076297605200> **Vote Miku.n to get `Loop` access** (12hrs)",colour=0x39138b)
                    await ctx.reply(embed=embed) 
        else:         
                    cat = "waifu"
                    crtlink=await god(cat)

                    embed = discord.Embed(colour=0x39138b)
                    embed.set_footer(text=f"{(a.name)} uWu ❣️ ",
                            icon_url=a.avatar_url)
                    embed.set_image(url=crtlink)
                    await ctx.send(embed=embed)  
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()

    async def holo(self,ctx):

        ppo = random.randint(0, 2)
        if ppo == 0:
            crtlink = (nekos.img("holo"))
        else:
                url = "https://nekobot.xyz/api/image?type=holo"
                r = requests.get(url)
                link = json.loads(r.text)
                crtlink = link["message"]
        embed = discord.Embed(colour=0x39138b)
        embed.set_image(url=crtlink)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()

    async def sfwkemo(self,ctx):
            url = "https://nekobot.xyz/api/image?type=kemonomimi"
            r = requests.get(url)
            link = json.loads(r.text)
            crtlink = link["message"]
            embed = discord.Embed(colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed,mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()

    async def neko(self,ctx):

        ppo = random.randint(0, 1)
        if ppo == 0:   
            cat = "neko"
            crtlink=await god(cat)
        else:
            crtlink = (nekos.img("neko"))
        embed = discord.Embed(colour=0x39138b)
        embed.set_image(url=crtlink)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()

    async def nekogif(self,ctx):
        crtlink = (nekos.img("ngif"))
        embed = discord.Embed(colour=0x39138b)
        embed.set_image(url=crtlink)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def foxgirl(self,ctx):
        crtlink = (nekos.img("fox_girl"))
        embed = discord.Embed(colour=0x39138b)
        embed.set_image(url=crtlink)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def pfp(self,ctx):
            crtlink = (nekos.img("avatar"))
            embed = discord.Embed(description=f"{ctx.message.author.mention} taje this pfp <:yami:878736933038219274>",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Example(client))
