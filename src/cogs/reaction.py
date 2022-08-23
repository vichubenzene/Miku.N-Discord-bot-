import discord
from discord.ext import commands
import requests
import json
import random
import nekos
from itertools import cycle

with open('sfw_json/jojo.json', 'r') as f:
    jo=cycle(json.load(f))
async def god(cat):
       url = f"https://api.waifu.pics/sfw/{cat}"
       r = requests.get(url)
       link = json.loads(r.text)
       crtlink = link["url"]
       return crtlink
class Example(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("reaction is ready")




    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def wave(self,ctx,member: discord.Member = None):
        cat = "wave"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Wave's at {member.mention} 🤠",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)}  Waves at you 🤠 ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)



    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def baka(self,ctx):
        crtlink = (nekos.img("baka"))
        embed = discord.Embed(colour=0x39138b)
        embed.set_image(url=crtlink)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def feed(self,ctx):
        crtlink = (nekos.img("feed"))
        embed = discord.Embed(colour=0x39138b)
        embed.set_image(url=crtlink)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def highfive(self,ctx,member: discord.Member = None):
        cat = "highfive"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} HighFive's {member.mention} 🤩",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} HighFive's you 🤩 ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)

            
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def glomp(self,ctx):

        base_url = "https://api.waifu.pics/"
        type = "sfw/"
        cat = "glomp"

        url = base_url + type + cat
        r = requests.get(url)
        link = json.loads(r.text)
        crtlink = link["url"]
        await ctx.reply(crtlink,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def slap(self,ctx,member: discord.Member = None):

        ppo = random.randint(0, 1)
        if ppo == 0:  
            base_url = "https://api.waifu.pics/"
            type = "sfw/"
            cat = "slap"

            url = base_url + type + cat
            r = requests.get(url)
            link = json.loads(r.text)
            crtlink = link["url"]

        else:
            crtlink = (nekos.img("slap"))
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} slapped {member.mention} 😱",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Slapped you 😱 ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)
    

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def bite(self,ctx,member: discord.Member = None):
        cat = "bite"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Bite's {member.mention} 😮",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Bite's you 😮 ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def nom(self,ctx):
        cat = "nom"
        crtlink=await god(cat)
        await ctx.reply(crtlink,mention_author=False)





    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def handhold(self,ctx,member: discord.Member = None):
        cat = "handhold"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Hold's {member.mention} Hand",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Hold's hand",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def happy(self,ctx):

        cat = "happy"
        crtlink=await god(cat)
        a=ctx.message.author
        a=ctx.message.author
        embed = discord.Embed(colour=0x39138b)
        embed.set_footer(text=f"{(a.name)} is Happy 😃",
                    icon_url=a.avatar_url)
        embed.set_image(url=crtlink)
        await ctx.reply(embed=embed,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def kick(self,ctx,member: discord.Member = None):
        cat = "kick"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Kick's {member.mention} 😨",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} kick's you 😨 ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def kill(self,ctx,member: discord.Member = None):
        cat = "kill"
        crtlink=await god(cat)
        a=ctx.message.author
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Killed {member.mention} 🔪",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Killed you 🔪 ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def wink(self,ctx,member: discord.Member = None):
        cat = "wink"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Wink's at {member.mention} 😉",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} 😉 ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)



    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def coffee(self,ctx):
                url = "https://nekobot.xyz/api/image?type=coffee"
                r = requests.get(url)
                link = json.loads(r.text)
                crtlink = link["message"]
                a=ctx.message.author
                embed = discord.Embed(colour=0x39138b)
                embed.set_footer(text=f"{(a.name)} Drinks ☕ ",
                            icon_url=a.avatar_url)
                embed.set_image(url=crtlink)
                await ctx.reply(embed=embed,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def cry(self,ctx):
        cat = "cry"
        crtlink=await god(cat)
        a=ctx.message.author
        a=ctx.message.author
        embed = discord.Embed(colour=0x39138b)
        embed.set_footer(text=f"{(a.name)} Cries 😭 ",
                    icon_url=a.avatar_url)
        embed.set_image(url=crtlink)
        await ctx.reply(embed=embed,mention_author=False)





    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def hug(self,ctx):
    

        ppo = random.randint(0, 1)
        if ppo == 0:   
            cat = "hug"
            crtlink=await god(cat)
            a=ctx.message.author
        else:
            crtlink = (nekos.img("hug"))
        
        a=ctx.message.author
        embed = discord.Embed(colour=0x39138b)
        embed.set_footer(text=f"{(a.name)} Hugs you❤️",
                    icon_url=a.avatar_url)
        embed.set_image(url=crtlink)
        await ctx.reply(embed=embed,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def kiss(self,ctx, member: discord.Member = None):
        # if not member:
        #     member = "Kisses you"
        ppo = random.randint(0, 1)
        if ppo == 0:  
            cat = "kiss"
            crtlink=await god(cat)
            a=ctx.message.author
            
        else:
            crtlink = (nekos.img("kiss"))
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} kisses {member.mention}😘",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Kisses you 😘",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def lick(self,ctx,member: discord.Member = None):
        cat = "lick"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Lick's {member.mention}",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Lick's you 😘",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)



    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def bonk(self,ctx,member: discord.Member = None):
        cat = "bonk"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Bonk's {member.mention} 😐",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Bonk's you 😐",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def pat(self,ctx,member: discord.Member = None):

        ppo = random.randint(0, 1)
        if ppo == 0:   
            cat = "pat"
            crtlink=await god(cat)
            a=ctx.message.author

        else:
            crtlink = (nekos.img("pat"))
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Pat's {member.mention} 🥰",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Pats's you 🥰",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def smug(self,ctx,member: discord.Member = None):
        ppo = random.randint(0, 1)
        if ppo == 0:   
            cat = "smug"
            crtlink=await god(cat)
            a=ctx.message.author
        else:
            crtlink = (nekos.img("smug"))
        
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} Smug's  {member.mention} 😏",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Smug 😏",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)



    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def yeet(self,ctx):
            cat = "yeet"
            crtlink=await god(cat)
            await ctx.reply(crtlink,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def blush(self,ctx,member: discord.Member = None):
        cat = "blush"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} blush's uWu {member.mention} 😍",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} blushes uWu 😍",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)



    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def smile(self,ctx,member: discord.Member = None):
        cat = "smile"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} smile's at {member.mention} 😄",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Smiling ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def cringe(self,ctx,member: discord.Member = None):
        cat = "cringe"
        crtlink=await god(cat)
        a=ctx.message.author
        try:
            embed = discord.Embed(description=f"{a.mention} 😒 {member.mention} ",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} 😒 ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)


    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.guild_only()
    async def poke(self,ctx,member: discord.Member = None):

        ppo = random.randint(0, 1)
        if ppo == 0:  
            cat = "poke"
            crtlink=await god(cat)
            a=ctx.message.author

        else:
            crtlink = (nekos.img("poke"))
        a=ctx.message.author

        try:
            embed = discord.Embed(description=f"{a.mention} Poke's {member.mention} ",colour=0x39138b)
            embed.set_image(url=crtlink)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(colour=0x39138b)
            embed.set_footer(text=f"{(a.name)} Poke's you ",
                        icon_url=a.avatar_url)
            embed.set_image(url=crtlink)
            await ctx.reply(embed=embed,mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def dance(self,ctx):
        cat = "dance"
        crtlink=await god(cat)
        a=ctx.message.author
        embed = discord.Embed(colour=discord.Color.dark_purple())
        embed.set_footer(text=f"{(a.name)} Dancing ",
                    icon_url=a.avatar_url)
        embed.set_image(url=crtlink)
        await ctx.send(embed=embed)






    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def jojo(self,ctx):
        crtlink = next(jo)
        a=ctx.message.author
        embed = discord.Embed(colour=discord.Color.dark_purple())
        embed.set_footer(text=f"{(a.name)} :  Everything is JOJO referance",
                    icon_url=a.avatar_url)
        embed.set_image(url=crtlink)
        await ctx.send(embed=embed)






    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def bully(self,ctx):
        cat = "bully"
        crtlink=await god(cat)
        a=ctx.message.author
        embed = discord.Embed(colour=0x360ba3)
        embed.set_footer(text=f"{(a.name)} bullies you ",
                    icon_url=a.avatar_url)
        embed.set_image(url=crtlink)
        await ctx.reply(embed=embed,mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def cuddle(self,ctx):
        ppo = random.randint(0, 2)
        if ppo == 0:
            crtlink = (nekos.img("cuddle"))
        else:
            cat = "cuddle"
            crtlink=await god(cat)
            a=ctx.message.author
        embed = discord.Embed(colour=0x39138b)
        embed.set_footer(text=f"{(a.name)} Cuddles you ❤️ ",
                    icon_url=a.avatar_url)
        embed.set_image(url=crtlink)
        await ctx.reply(embed=embed,mention_author=False)
    
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def tickle(self,ctx,member: discord.Member = None):
        crtlink = (nekos.img("tickle"))
        a=ctx.message.author
        try:
                    embed = discord.Embed(description=f"{a.mention} tickle's {member.mention} 🤪",colour=0x39138b)
                    embed.set_image(url=crtlink)
                    await ctx.send(embed=embed)
        except:
                    embed = discord.Embed(colour=0x39138b)
                    embed.set_footer(text=f"{(a.name)} tickle's you 🤪 ",
                                icon_url=a.avatar_url)
                    embed.set_image(url=crtlink)
                    await ctx.reply(embed=embed,mention_author=False)
def setup(client):
    client.add_cog(Example(client))