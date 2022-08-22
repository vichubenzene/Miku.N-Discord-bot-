import discord
from discord.ext import commands
import requests
import json
import random
from jikanpy import jikan
aki = jikan.Jikan()
class Example(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("quotes is ready")



    @commands.command(aliases = ["quote","quotes"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def raquote(self,ctx):
        url = 'https://animechan.vercel.app/api/random'
        test = requests.get(url).json()
        character = test['character']
        anime = test['anime']
        quote = test['quote']

        asi = aki.search('anime', anime, page=1)
        pic = (asi['results'][0]['image_url'])

        embed = discord.Embed(
            title=quote,
            description=(f'Anime :   {anime}\n\nCharacter :  {character}\n\n'),
            colour=0x19198c
        )

        embed.set_thumbnail(url=pic)
        embed.set_footer(text=ctx.message.author.name,
                                    icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)




    @commands.command(aliases = ["animequote","animequotes"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def aquote(self,ctx, *, name=""):

        if name=="":
            await ctx.send("Use anime name `m.aquote naruto` <a:heart3:879888752594530425>")
        else:
#             asi = aki.search('anime', name, page=1)

#             name = (asi['results'][0]['title'])
            info = (f'https://animechan.vercel.app/api/quotes/anime?title={name}')
            url = info
            data = requests.get(url).json()

            if (len(data) == 1):
                await ctx.send(data['error'])

            else:
                i = random.randint(0, len(data) - 1)
                test = data[i]

                character = test['character']
                anime = test['anime']
                quote = test['quote']

                asi = aki.search('anime', anime, page=1)
                pic = (asi['results'][0]['image_url'])

                embed = discord.Embed(
                    title=quote,
                    description=(f'Anime :   {anime}\n\nCharacter :  {character}\n\n'),
                    colour=0x19198c
                )
                embed.set_thumbnail(url=pic)
                embed.set_footer(text=ctx.message.author.name,
                                    icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)


    # REQ:CHARACTER QUOTE
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def cquote(self,ctx, *, name=""):
        if name=="":
            await ctx.send("Use anime name `m.aquote naruto` <a:heart3:879888752594530425>")
        else:
            info = (f'https://animechan.vercel.app/api/quotes/character?name={name}')
            url = info
            data = requests.get(url).json()

            if (len(data) == 1):
                await ctx.send(data['error'])

            else:
                i = random.randint(0, len(data) - 1)
                test = data[i]

                character = test['character']
                anime = test['anime']
                quote = test['quote']

                asi = aki.search('anime', anime, page=1)
                pic = (asi['results'][0]['image_url'])

                embed = discord.Embed(
                    title=quote,
                    description=(f'Anime :   {anime}\n\nCharacter :  {character}\n\n'),
                    colour=0x19198c
                )
                embed.set_thumbnail(url=pic)
                embed.set_footer(text=ctx.message.author.name,
                                    icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)


    # INSPIRE QUOTE
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def inspire(self,ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)



        embed = discord.Embed(
            title=json_data[0]['q'],
            description=f"  - {json_data[0]['a']}",
            colour=0x19198c
        )
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/424792877546340372/878663313611952148/80.png')
        embed.set_footer(text=ctx.message.author.name,
                            icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))
