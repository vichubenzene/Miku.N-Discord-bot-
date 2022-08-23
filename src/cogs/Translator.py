import discord
from discord.ext import commands
import random
from datetime import datetime
import json
import requests
from translator.benzene_translator import google_translator
class Example(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Translator is ready")


    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.guild_only()
    async def lcode(self,ctx):
        user = ctx.author
        a = "**#A**\n\nAfrikaans `af` \nAlbanian `sq`\n Amharic `am`\n Arabic `ar` \nArmenian `hy`\n Azerbaijani `az`\n\n**#B**\n\n Basque `eu` \nBelarusian `be` \nBengali `bn` \nBosnian `bs` \nBulgarian `bg`\n\n**#C**\n\n Catalan `ca` \nCebuano `ceb` \nChinese (Simplified) `zh-CN or zh` \nChinese (Traditional) `zh-TW` \nCorsican `co`\n Croatian `hr`\n Czech `cs` \n\n**#D**\nDanish `da` \nDutch `nl` \n\n**#E**\n\nEnglish `en`\nEsperanto `eo`\nEstonian `et`\n\n **#F**\n\nFinnish `fi`\n French `fr`\n Frisian `fy`\n\n **#G**\n\nGalician `gl` \nGeorgian `ka`\n German `de`\n Greek `el` \nGujarati `gu`\n\n**#H**\n\n Haitian Creole `ht`\n Hausa `ha`\n Hawaiian `haw`\n Hebrew `he or iw`\n Hindi `hi`\n Hmong `hmn`\n Hungarian `hu`\n\n **#I**\n\nIcelandic `is`\nIgbo `ig`\n Indonesian `id`\n Irish `ga`\n Italian `it`\n\n**#J**\n\nJapanese `ja`\n Javanese `jv`\n\n**#K**\n\n Kannada `kn`\n Kazakh `kk`\n Khmer `km`\n Kinyarwanda `rw`\nKorean `ko`\n Kurdish `ku`\n Kyrgyz `ky`\n\n**#L**\n\n Lao `lo`\n Latin `la`\n Latvian `lv`\n Lithuanian `lt`\n Luxembourgish `lb`\n\n **#M**\n\nMacedonian `mk`\n Malagasy `mg`\n Malay `ms`\nMalayalam `ml`\n Maltese `mt`\n Maori `mi`\n Marathi `mr`\n Mongolian `mn`\n Myanmar (Burmese) `my`\n\n**#N**\n\n Nepali `ne`\n Norwegian `no`\n Nyanja (Chichewa) `ny`\n\n**#O**\n\n Odia (Oriya) `or`\n\n**#P**\n\n Pashto `ps`\n Persian `fa`\n Polish `pl`\n Portuguese (Portugal Brazil) `pt`\n Punjabi `pa`\n Romanian `ro`\n\n **#R**\n\nRussian `ru`\n\n **#S**\n\nSamoan `sm`\n Scots Gaelic `gd`\n Serbian `sr`\n Sesotho `st`\n Shona `sn`\n Sindhi `sd`\n Sinhala (Sinhalese) `si`\n Slovak `sk`\n Slovenian `sl`\n Somali `so`\n Spanish `es`\n Sundanese `su`\n Swahili `sw`\n Swedish `sv`\n\n**#T**\n\n Tagalog (Filipino) `tl`\n Tajik `tg`\n Tamil `ta`\n Tatar `tt`\n Telugu `te`\n Thai `th`\n Turkish `tr`\n Turkmen `tk`\n\n**#U**\n\n Ukrainian `uk`\n Urdu `ur`\n Uyghur `ug`\n Uzbek `uz`\n\n**#V**\n\n Vietnamese `vi`\n\n**#W**\n\n Welsh `cy`\n \n**#X**\n\nXhosa `xh`\n \n**#Y**\n\nYiddish `yi`\n\nYoruba `yo` \n\n**#Z**\n\nZulu `zu`\n\n **This is not `spam` this is the `universal language code`**"
        await ctx.send(
            f"check your dm for `language codes` recoganized by `Google` {user.mention}\n\ncommand: `m.lang ta hello` for tamil,\t`m.lang en வணக்கம்` for english"
        )
        await user.send(a)


    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def meaning(self,ctx, *, name=""):
        if name=="":
                await ctx.send("Give words eg: `m.meaning word` <a:heart3:879888752594530425>")
        else:
            em = discord.Embed( title=f"`{name}` :shinto_shrine: ",colour=0x39138b)
            base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            cat = name
            url = base_url + cat
            r = requests.get(url)
            link = json.loads(r.text)
            ta = link[0]
            definition = (ta["meanings"][0]["definitions"][0]["definition"])

            em.add_field(name='Definition', value=f"`{definition}`", inline=False)
            em.set_footer(text=(ctx.message.author.name),
                        icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=em)

    @commands.command(aliases=["trans", "translate", "language"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    async def lang(self,ctx, arg1, *, arg2):

        detector = google_translator()
        detect_result = detector.detect(arg2)
        translator = google_translator()
        pronounce = translator.translate(arg2,
                                        lang_src=detect_result,
                                        lang_tgt=arg1,
                                        pronounce=True)
        if pronounce[2] is None:
                em = discord.Embed( title= f"<:02Cozy:878167184705204225> lang = {detect_result[1]}",description=f"> {pronounce[0]}\n\n> {pronounce[1]}",colour=0x39138b)
                await ctx.send(embed=em)
        else:
                em = discord.Embed( title= f"<:02Cozy:878167184705204225> lang = {detect_result[1]}",description=f"> {pronounce[0]}\n\n> {pronounce[2]}",colour=0x39138b)
                await ctx.send(embed=em)


def setup(client):
    client.add_cog(Example(client))
