import discord
from discord.ext import commands
import requests
import urllib.parse
from pysaucenao import DailyLimitReachedException, AnimeSource, UnknownStatusCodeException, GenericSource, \
    InvalidImageException, InvalidOrWrongApiKeyException, MangaSource, SauceNao, SauceNaoException, \
    ShortLimitReachedException, VideoSource
from pysaucenao.containers import ACCOUNT_ENHANCED, AnimeSource, BooruSource, PixivSource
import re,random
from urllib import parse
from disputils import *
import requests, bs4
from bs4 import BeautifulSoup as soup
import lxml

class mikufinder(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def find(self,ctx, *,arg=""):
        if arg=="":
            for file in ctx.message.attachments:
                arg=file.url
        a=requests.get("https://api.trace.moe/search?url={}".format(urllib.parse.quote_plus(arg))
             ).json()
        a=a['result']
        b=""
        flag=[]
        for i in range(0,len(a)):
            if a[i]['anilist'] not in flag:
                flag=[a[i]['anilist']] + flag
                b=b+f"> {len(flag)}. ID: {a[i]['anilist']},  **`{a[i]['filename']}`**,  `ep: {a[i]['episode']}`, time: {a[i]['from']} - {a[i]['to']},  match: {int(float(a[i]['similarity'])*100)}%, Samples: [Video]({a[i]['video']}), [Image]({a[i]['image']})\n\n"
                if len(c)>4095:
                    break
                b=c
        embed = discord.Embed(
                    title=f"Found {len(flag)} Matches" ,
                    description=(b),timestamp=(ctx.message.created_at),
                    colour=0x19198c)
        embed.set_thumbnail(url=arg)
        embed.set_footer(text=ctx.message.author.name,
                                 icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
    async def get_sauce_embeds(self, ctx, url, results):
        embeds = []
        google_url = f"https://www.google.com/searchbyimage?image_url={url}&safe=off"
        yandex_url = f"https://yandex.com/images/search?url={url}&rpt=imageview"
        saucenao_url = f"https://saucenao.com/search.php?url={url}"
        for sauce in results:
            try:
                embed = discord.Embed(timestamp=(ctx.message.created_at),
                    colour=0x19198c)
                thumbnail = ctx.author.avatar_url if not sauce.thumbnail else sauce.thumbnail
                similarity = 0 if not sauce.similarity else sauce.similarity
                if similarity > 80:
                    review = "Hey found something highly similar to your query. Result seems to be identical."
                if similarity > 60 and similarity < 80:
                    review = "Not so sure if this is the correct result."
                if similarity < 60:
                    review = "Probably not the correct result but still take it."

                if isinstance(sauce.urls, list):
                    embed.add_field(name="Sauce(s)", value="\n".join(sauce.urls), inline=False)
                else:
                    if sauce.urls:
                        embed.add_field(name="Sauce", value=f"{sauce.urls}")
                    else:
                        source = "https://saucenao.com/search.php?url={}".format(parse.quote_plus(url))
                        embed.add_field(name="Sauce",
                                        value=f"Sauce not given man :(. Still try by going [Here]({source})",
                                        inline=False)
                if isinstance(sauce, AnimeSource):
                    await sauce.load_ids()
                    embed.add_field(name="Anime Info", value=f"[AniList]({sauce.anilist_url}) "
                                                             f"[MyAnimeList]({sauce.mal_url})")
                if isinstance(sauce, VideoSource):
                    embed.add_field(name="Episode ", value=sauce.episode)
                    embed.add_field(name="TimeStamp", value=sauce.timestamp, inline=False)

                if isinstance(sauce, MangaSource):
                    embed.add_field(name="Chapter", value=sauce.chapter if sauce.chapter else "Not given")
                author = "Author not given" if not sauce.author_name else sauce.author_name
                title = "Title not given" if not sauce.title else sauce.title

                index_id = "Index not given" if (sauce.index_id == None) else sauce.index_id
                index_name = "Inxed name not given" if (sauce.index_name == None) else sauce.index_name

                embed.description = f"Sucessfully found closest image(`{title}`) with the following information."
                embed.add_field(name="Similarity", value=similarity)
                if isinstance(sauce, PixivSource):
                    embed.add_field(name="Author", value=f"[{author}]({sauce.author_url})")
                embed.add_field(name="Author", value=author)
                embed.add_field(name="Index", value=f"ID : `{index_id}` \nName : `{index_name}`", inline=False)
                if not url.startswith(("https://konachan", "https://yan")):
                    embed.add_field(name="Others", value=f"<:Google:989929285726920724> [Google]({google_url}) "
                                                         f"<:yandex:989929416803110932> [Yandex]({yandex_url}) "
                                                         f"<:saucenao:989930050138800189> [SauceNao]({saucenao_url})", inline=False)
                embed.add_field(name="Miku says:", value=review)
                embed.set_thumbnail(url=thumbnail)
                embeds.append(embed)
            except:
                pass
        return embeds

    @commands.command(aliases=['saucenao'])
    @commands.guild_only()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def sauce(self, ctx, url=None):
        # https://github.com/FujiMakoto/pysaucenao Pray to the lord and savior
        if url != None:
            if self.is_url(url) != True:
                return await ctx.send(
                    "Your image url doesn't seem to be accurate. An image url should look like `https://danbooru.donmai.us/data/original/a2/d0/a2d093a060757d36d8a9f03bcbfbcd82.jpg`.")

        if url == None:
            try:
                url = ctx.message.attachments[0].url
            except:
                url = None

        if url == None:
            await ctx.send("Couldn't find the url checking for the last message with image url.", delete_after=5)
            async for message in ctx.channel.history(limit=10):
                check = self.is_url(message.content)
                if check == True:
                    url = message.content
                    break
        if url == None:
            return await ctx.send("No image urls found in the last 10 messages please retry by uploading one.")
        if url.endswith(('.mp4', '.webm', '.mov')):
            if url.startswith('https://cdn.discordapp.com') or url.startswith('https://media.discordapp.net'):
                url = url.replace("cdn.discordapp.com", "media.discordapp.net") + "?format=jpeg"
            else:
                return await ctx.send(
                    "If you are getting a video sauce, please use a discord url. Just download the video from this link and upload it to discord while using `m.sauce`.")

        saucenao_url = f"https://saucenao.com/search.php?url={url}"
        try:
            sauce = SauceNao(api_key='2c89779a50f401af9e0caaacb5299dab88dc0b84', priority=[21, 22, 5, 37, 25])
            results = await sauce.from_url(url)
            embeds = await self.get_sauce_embeds(ctx, url, results)
        except SauceNaoException:
            return await self.generic_error(ctx, saucenao_url)
        except DailyLimitReachedException:
            return await self.daily_error(ctx)
        except:
            pass
        if embeds:
            a = paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()
        elif not embeds:
                a=requests.get("https://api.trace.moe/search?url={}".format(urllib.parse.quote_plus(url))
                ).json()
                print(a)
                a=a['result']
                print(a[1]['anilist'])
                b=""
                flag=[]
                for i in range(0,len(a)):
                        if a[i]['anilist'] not in flag:
                            flag=[a[i]['anilist']] + flag
                            
                            
                            c=b+f"> {len(flag)}. ID: {a[i]['anilist']},  **`{a[i]['filename']}`**,  `ep: {a[i]['episode']}`, time: {a[i]['from']} - {a[i]['to']},  match: {int(float(a[i]['similarity'])*100)}%, Samples: [Video]({a[i]['video']}), [Image]({a[i]['image']})\n\n"
                            if len(c)>4095:
                                break
                            b=c
                embed = discord.Embed(
                                title=f"Found {len(flag)} Matches" ,
                                description=(b),timestamp=(ctx.message.created_at),
                                colour=0x19198c)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=ctx.message.author.name,
                                            icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)
                return await self.generic_error(ctx, saucenao_url)
#     @commands.command(aliases=['sauceadv'])
#     @commands.cooldown(1, 15, commands.BucketType.user)
#     async def sauceadvanced(self, ctx, url= None):
#         if url:
#             if self.is_url(url) != True:
#                 return await ctx.send(
#                     "Your image url doesn't seem to be accurate. An image url should look like `https://danbooru.donmai.us/data/original/a2/d0/a2d093a060757d36d8a9f03bcbfbcd82.jpg`.")

#         if url == None:
#             await ctx.send("No url found in command, checking for attachments.", delete_after=5)
#             try:
#                 url = ctx.message.attachments[0].url
#             except:
#                 url = None

#         if url == None:
#             await ctx.send("Couldn't find the url checking for the last message with image url.", delete_after=5)
#             async for message in ctx.channel.history(limit=10):
#                 check = self.is_url(message.content)
#                 if check == True:
#                     url = message.content
#                     break
#         if url == None:
#             return await ctx.send("No image urls found in the last 10 messages please retry by uploading one.")
#         if url.endswith(('.mp4', '.webm', '.mov')):
#             if url.startswith(('https:cdn.discordapp.com', 'https://media.discordapp.net')):
#                 url = url.replace("cdn.discordapp.com", "media.discordapp.net") + "?format=jpeg"
#             else:
#                 return await ctx.send(
#                     "If you are getting a video sauce, please use a discord url. Just download the video from this link and upload it to discord while using `dh sauceadv`.")

#         r = requests.get(f"https://imgops.com/{url}").text
#         soup1 = soup(r, 'lxml')
#         print(soup1)
#         karmadecay = soup1.find("a", {"id": "t87"})['href']
#         print(karmadecay)
#         iqdb = soup1.find("a", {"id": "t78"})['href']
#         print(iqdb)
#         saucenao = soup1.find("a", {"id": "t82"})['href']
#         print(saucenao)
#         ascii2d = "https://imgops.com" + soup1.find("a", {"id": "t84"})['href']
#         tracemoe = soup1.find("a", {"id": "t201"})['href']
#         print(tracemoe)
#         google_url = f"https://www.google.com/searchbyimage?image_url={url}&safe=off"
#         print(google_url)
#         embed = discord.Embed()
#         embed.set_thumbnail(url=url)
#         embed.add_field(name="SauceNao", value=f"[Click Here]({saucenao})", inline=False)
#         embed.add_field(name="Ascii2d", value=f"[Click Here]({ascii2d})", inline=False)
#         embed.add_field(name="Reddit", value=f"[Click Here]({karmadecay})", inline=False)
#         embed.add_field(name="Tracemoe", value=f"[Click Here]({tracemoe})", inline=False)
#         embed.add_field(name="IQDB", value=f"[Click Here]({iqdb})", inline=False)
#         print("p")
#         embed.add_field(name="Google", value=f'[Click Here]({google_url})', inline=False)
#         embed.set_footer(icon_url=ctx.author.avatar_url,
#                          text="This data is from imageops.com, please refer there for more cool image operaions.")
#         await ctx.send(embed=embed)

    def is_url(self, message):
        pattern = re.compile(r"^https?://\S+(\.jpg|\.png|\.jpeg|\.webp|\.gif|\.mp4|\.mov|\.webm)$")
        if not pattern.match(message):
            return False
        return True

    async def generic_error(self, ctx, url):
        em = discord.Embed(description=f"Sorry, nothing very accurate found you can try [here]({url}) if you'd like.\n we have provided with `m.find`",timestamp=(ctx.message.created_at),
                    colour=0x19198c)
        em.set_footer(text="Also, make sure your url ends with an image format.")
        await ctx.send(embed=em)
    async def daily_error(self, ctx, url):
        em = discord.Embed(description=f"Sorry, Daily limit of 100 request has been reached for <@876139135507763280>\n Donate by `M.donate` for improvements\n we have provided with `m.find`",timestamp=(ctx.message.created_at),
                    colour=0x19198c)
        em.set_footer(text="Help my Master Get a Body pillow uWu")
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(mikufinder(client))
