import discord
from discord.ext import commands
import requests
import json
import lxml
import validator
import random
import asyncio
import html
import topgg

dbl_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijg3NjEzOTEzNTUwNzc2MzI4MCIsImJvdCI6dHJ1ZSwiaWF0IjoxNjMzODA0NzYzfQ.xMREbcyBUSTyTAM_ygWaiAvT9a4SlmEGrVQjRCS_xjs"
with open('img.json', 'r') as f:
    question_img = json.load(f)


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("quiz is ready")

    @commands.command(aliases=["p"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def points(self, ctx):
        await open_account(ctx.author)
        user = ctx.author

        users = await get_bank_data()
        questions = users[str(user.id)]["number"]

        wallet_amt = users[str(user.id)]["wallet"]

        em = discord.Embed(title=f'{ctx.author.name} <a:CH_KannaLove:895920700114755594> ', color=discord.Color.red())
        em.add_field(name="points", value=wallet_amt)
        em.add_field(name='total question', value=questions)
        em.set_footer(text=f"{self.client.user} quiz points", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def privacy(self, ctx):
        em = discord.Embed(title=f'{ctx.author.name} <a:CH_KannaLove:895920700114755594> ',
                           description="Quiz privacy policy:\nMiku.N#0211 Track's the user's presence status and messages of a person for 8 seconds when other people in the same server are using this bot for playing quiz.They are started tracking once they have started to play the game by using `m.quiz`.They can delete the history and remove this tracking if they don't want to play the bot by using `m.delete`\n\nwe only store user id \nwe don't store any message content data's which are checked for 8 seconds\nwe dont use any 3rd party storage for this\nJoin support server for more info about your privacy and storage information\n https://discord.gg/cyKAjwcZdB", color=discord.Color.red())
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def delete(self, ctx):
        user = ctx.author
        await ctx.send(
            f"your score details has been deleted {ctx.author.mention}, if you have intrest in getting it back, you can apply for it in support server with previous screeshot proof")

        with open('mainbank.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(user.id))

        with open('mainbank.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.command(aliases=["lb"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def leaderboard(self, ctx, x=5):
        users = await get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total, reverse=True)

        em = discord.Embed(title=f"Top {x} ranks <:kanna_inspect:878150112457687040>",
                           description="This is decided on the total score", color=discord.Color(0xfa43ee))
        index = 1

        for amt in total:
            id_ = leader_board[amt]
            member = await self.client.fetch_user(id_)
            if index == 1:
                em.add_field(name=f"{index}. {member} 👑",
                             value=f'`{amt} points from {users[str(id_)]["number"]} questions`', inline=False)
                em.set_footer(text=f"current 👑 holder {member}", icon_url=member.avatar_url)
            elif index == 2:
                em.add_field(name=f"{index}. {member} 🥈",
                             value=f'`{amt} points from {users[str(id_)]["number"]} questions`', inline=False)
            elif index == 3:
                em.add_field(name=f"{index}. {member} 🥉",
                             value=f'`{amt} points from {users[str(id_)]["number"]} questions`', inline=False)
            elif index == 4:
                em.add_field(name=f"{index}. {member} 🎖️",
                             value=f'`{amt} points from {users[str(id_)]["number"]} questions`', inline=False)
            else:
                em.add_field(name=f"{index}. {member}",
                             value=f'`{amt} points  from {users[str(id_)]["number"]} questions`', inline=False)
            if index == x:
                break
            else:
                index += 1
        em.add_field(name="👑 Holder recieve Spl features",
                     value="from support [server](https://discord.gg/cyKAjwcZdB) on month end🎀 • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands)",
                     inline=False)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def quiz(self, ctx, user=discord.Member):
        author = ctx.message.author
        print(author)
        if not user.bot:
            await ctx.send("unnakenna pa bot yellam pannuva")

        else:
            qw = 1
            if await self.client.topgg.get_user_vote(user_id=ctx.author.id):
                print("hi")
                qw = 2
                af = f"Thx for voting you can get `2 times` the score`{author.name}`\n[Vote here](https://top.gg/bot/876139135507763280/vote)    <:done:895759484503334962> • [Invite Bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) ✨"

            else:
                af = f"Vote to get `2 times` the score`{author.name} `\n[Vote here](https://top.gg/bot/876139135507763280/vote) <:upvote:893317076297605200> • [Invite Bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) BOT✨"
            print(ctx.author)

            users = await get_bank_data()
            author = ctx.message.author
            pic = author.avatar_url
            base_url = "https://opentdb.com/api.php?amount=1&type=multiple"
            category = "&category=31"
            embed = discord.Embed(
                title=(f"Welcome to the Anime/Manga Quiz Game\n {author.name} <:What:878153160747794492>"),
                description=(
                    f"This is a mulitple choice game and you `decide` the difficulty!\n\n**\t🇪\tEasy **\t,**\t\t🇲\tMedium  \t**, **\t\t🇭\tHard **\n `react your option {author.name}`"),
                colour=discord.Colour.blurple()
            )

            # embed.add_field(name="** **", value= af)
            embed.set_thumbnail(
                url=random.choice(question_img))
            embed.set_footer(text="answer within 30s  • DM me m.invite to invite",
                             icon_url=pic)
            message = await ctx.send(embed=embed)

            await message.add_reaction("🇪")
            await message.add_reaction("🇲")
            await message.add_reaction("🇭")

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["🇪", "🇲",
                                                                      "🇭"] and message.id == reaction.message.id

            a = 1
            while (a == 1):
                try:
                    reaction, user = await self.client.wait_for("reaction_add", timeout=30, check=check)

                    if str(reaction.emoji) == "🇪":
                        difficulty = "easy"
                        d = 10
                        a = 0
                        try:

                            await message.remove_reaction(reaction, user)

                        except:
                            print("hi")



                    elif str(reaction.emoji) == "🇲":
                        difficulty = "medium"
                        d = 15
                        a = 0
                        try:
                            await message.remove_reaction(reaction, user)

                        except:
                            print("hi")

                    elif str(reaction.emoji) == "🇭":
                        difficulty = "hard"
                        d = 20
                        a = 0
                        try:
                            await message.remove_reaction(reaction, user)
                        except:
                            print("hi")
                    else:
                        try:
                            await message.remove_reaction(reaction, user)
                        except:
                            print("hi")

                except asyncio.TimeoutError:
                    await message.clear_reactions()
                    return
            difficulty = "&difficulty=" + difficulty
            r = requests.get(base_url + category + difficulty)
            if (r.status_code != 200):
                await ctx.send("\nSorry could not retrieve data. Press Enter to try again.")
            else:

                await open_account(ctx.author)

                user = ctx.author

                users = await get_bank_data()

                users[str(user.id)]["number"] += 1

                with open("mainbank.json", 'w') as f:
                    json.dump(users, f, indent=4)

                question = json.loads(r.text)
                choices = question["results"][0]["incorrect_answers"]
                correct = question["results"][0]["correct_answer"]
                choices.append(correct)
                random.shuffle(choices)
                c_count = 0

                embed = discord.Embed(title=(html.unescape(question["results"][0]["question"])),
                                      description=" <:QuestionsWut:878155721546547250> ",
                                      colour=discord.Colour(0x71368a)
                                      )
                embed.set_thumbnail(
                    url=random.choice(question_img))
                embed.set_footer(text="answer within 30s  • DM me m.invite to invite",
                                 icon_url=pic)

                for choice in choices:
                    c_count += 1
                    embed.add_field(name=(f"[ {str(c_count)}]   {html.unescape(choice)}  "), value=("** **"),
                                    inline=False)
                embed.add_field(name="** **", value=af, inline=True)
                await message.edit(embed=embed)
                try:
                    await message.clear_reactions()
                    await message.add_reaction("1️⃣")
                    await message.add_reaction("2️⃣")
                    await message.add_reaction("3️⃣")
                    await message.add_reaction("4️⃣")
                except:
                    await message.add_reaction("🎉")
                    await message.add_reaction("1️⃣")
                    await message.add_reaction("2️⃣")
                    await message.add_reaction("3️⃣")
                    await message.add_reaction("4️⃣")

                def acheck(reaction, user):
                    return user == ctx.author and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣",
                                                                          "4️⃣"] and message.id == reaction.message.id

                a = 1
                while (a == 1):
                    try:
                        reaction, user = await self.client.wait_for("reaction_add", timeout=30, check=acheck)

                        if str(reaction.emoji) == "1️⃣":
                            answer = 1
                            a = 0

                        elif str(reaction.emoji) == "2️⃣":
                            answer = 2
                            a = 0

                        elif str(reaction.emoji) == "3️⃣":
                            answer = 3
                            a = 0

                        elif str(reaction.emoji) == "4️⃣":
                            answer = 4
                            a = 0


                    except asyncio.TimeoutError:
                        await message.clear_reactions()
                        embed = discord.Embed(title=(html.unescape(question["results"][0]["question"])),
                                              colour=discord.Colour.dark_gold()
                                              )
                        embed.set_thumbnail(
                            url=random.choice(question_img))
                        embed.set_footer(text=f"✨Answer : {html.unescape(correct)} 🎀",
                                         icon_url=pic)
                        c_count = 0
                        for choice in choices:
                            c_count += 1
                            embed.add_field(name=(f"[ {str(c_count)}]   {html.unescape(choice)}  "), value=("** **"),
                                            inline=False)
                        embed.add_field(name="**late**  <:TokitoPopcorn:878162297783222282>",
                                        value=f"Time up {author.name} !!", inline=True)

                        await message.edit(embed=embed)
                        break
                if (choices[answer - 1] == correct):
                    user = ctx.author

                    users = await get_bank_data()

                    earning = d * qw

                    embed = discord.Embed(title=(html.unescape(question["results"][0]["question"])),
                                          colour=discord.Colour.dark_green()
                                          )
                    embed.set_thumbnail(
                        url=random.choice(question_img))
                    embed.set_footer(text=f"✨Answer : {html.unescape(correct)} 🎀",
                                     icon_url=pic)
                    # c_count=0
                    # for choice in choices:
                    #     c_count += 1
                    #     embed.add_field(name=(f"[ {str(c_count)}]   {html.unescape(choice)}  "), value=("** **"), inline=False)
                    embed.add_field(name="** **",
                                    value=f"Good job! You are correct!<:02Yay:878157685483261992> {author.name}",
                                    inline=True)
                    embed.add_field(name=f"**Points = {earning}**", value=af, inline=False)
                    await message.edit(embed=embed)

                    users[str(user.id)]["wallet"] += earning
                    with open("mainbank.json", 'w') as f:
                        json.dump(users, f, indent=4)


                else:
                    user = ctx.author

                    users = await get_bank_data()

                    earning = d

                    embed = discord.Embed(title=(html.unescape(question["results"][0]["question"])),
                                          colour=discord.Colour.red()
                                          )
                    embed.set_thumbnail(
                        url=random.choice(question_img))
                    embed.set_footer(text=f"✨Answer : {html.unescape(correct)} 🎀",
                                     icon_url=pic)
                    c_count = 0
                    for choice in choices:
                        c_count += 1
                        embed.add_field(name=(f"[ {str(c_count)}]   {html.unescape(choice)}  "), value=("** **"),
                                        inline=False)
                    embed.add_field(name="** **", value=f"wrong {author.name} <a:AniCry:878161279716577360> ",
                                    inline=True)
                    earning = 4 * qw
                    embed.add_field(name=f"**Points = {earning}**", value=af, inline=False)
                    await message.edit(embed=embed)

                    users[str(user.id)]["wallet"] += earning
                    with open("mainbank.json", 'w') as f:
                        json.dump(users, f, indent=4)
                channel = self.client.get_channel(988420077177171998)
                await channel.send(f'<@{ctx.author.id}> `{ctx.channel.name}`  `{ctx.guild}`',
                                   file=discord.File("mainbank.json"))
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def privacy(self, ctx):
        em = discord.Embed(title=f'{ctx.author.name} <a:CH_KannaLove:895920700114755594> ',
                           description="Quiz privacy policy:\nMiku.N#0211 Track's the user's presence status and messages of a person for 8 seconds when other people in the same server are using this bot for playing quiz.They are started tracking once they have started to play the game by using `m.quiz`.They can delete the history and remove this tracking if they don't want to play the bot by using `m.delete`\n\nwe only store user id \nwe don't store any message content data's which are checked for 8 seconds\nwe dont use any 3rd party storage for this\nJoin support server for more info about your privacy and storage information\n https://discord.gg/cyKAjwcZdB", color=discord.Color.red())
        await ctx.send(embed=em)
        
    @commands.command(aliases=["quotesquiz", "quizquote", "quizquotes"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def quotequiz(self, ctx, *, name=""):
        if name == "":
            await ctx.send("Use `m.quotequiz naruto` <a:heart3:879888752594530425>"
                           )
        else:
            user = ctx.author

            users = await get_bank_data()
            author = ctx.message.author
            print(author)
            if author.bot:
                await ctx.send("unnakenna pa bot yellam pannuva")

            else:
                qw = 1
                if await self.client.topgg.get_user_vote(user_id=ctx.author.id):
                    qw = 2
                    af = f"Thx for voting you can get `2 times` the score`{author.name}`\n[Vote here](https://top.gg/bot/876139135507763280/vote)  <:done:895759484503334962> • [Invite Bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) ✨"

                else:
                    af = f"Vote to get `2 times` the score`{author.name} `\n[Vote here](https://top.gg/bot/876139135507763280/vote) <:upvote:893317076297605200> • [Invite Bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) BOT✨"
                author = ctx.message.author
                pic = author.avatar_url
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
                    i2 = random.randint(0, len(data) - 1)
                    test = data[i2]
                    character2 = test['character']
                    i3 = random.randint(0, len(data) - 1)
                    test = data[i3]
                    character3 = test['character']
                    i4 = random.randint(0, len(data) - 1)
                    test = data[i4]
                    character4 = test['character']
                    u = 1
                    if (character == character2):
                        for i in range(0, len(data) - 1):
                            test = data[i]
                            character5 = test['character']
                            if character5 != character:
                                character2 = character5
                                break
                            else:
                                if u == 1:
                                    await ctx.send(
                                        f"Sorry there is only one character `{character}` in our data base try again later")
                                    u = 0
                    if (character == character3):
                        for i in range(0, len(data) - 1):
                            test = data[i]
                            character5 = test['character']
                            if character5 != character:
                                character3 = character5
                                break
                            else:
                                if u == 1:
                                    await ctx.send(
                                        f"Sorry there is only one character `{character}` in our data base try again later")
                                    u = 0
                    if (character == character4):
                        for i in range(0, len(data) - 1):
                            test = data[i]
                            character5 = test['character']
                            if character5 != character:
                                character4 = character5
                                break
                            else:
                                if u == 1:
                                    await ctx.send(
                                        f"Sorry there is only one character `{character}` in our data base try again later")
                                    u = 0

                    em = discord.Embed(title=f"Anime : {anime}",
                                       description=f"{quote} ", colour=0x19198c)
                    g = random.randint(0, 3)
                    if g == 0:
                        em.add_field(name="Who said these <:What:878153160747794492>",
                                     value=f"\n1️⃣ {character}\n2️⃣ {character2}\n3️⃣ {character3}\n4️⃣ {character4}",
                                     inline=True)
                    elif g == 1:
                        em.add_field(name="Who said these <:What:878153160747794492>",
                                     value=f"\n1️⃣{character2} \n2️⃣ {character} \n3️⃣ {character3}\n4️⃣ {character4}",
                                     inline=True)
                    elif g == 2:
                        em.add_field(name="Who said these <:What:878153160747794492>",
                                     value=f"\n1️⃣{character4} \n2️⃣ {character2} \n3️⃣ {character}\n4️⃣ {character3}",
                                     inline=True)
                    else:
                        em.add_field(name="Who said these <:What:878153160747794492>",
                                     value=f"\n1️⃣{character3} \n2️⃣ {character2} \n3️⃣ {character4}\n4️⃣ {character}",
                                     inline=True)
                    em.set_thumbnail(
                        url=random.choice(question_img))

                    em.set_footer(text="answer within 30s  • DM me m.invite to invite",
                                  icon_url=pic)

                    em.add_field(name="** **", value=af, inline=False)
                    message = await ctx.send(embed=em)
                    await message.add_reaction("1️⃣")
                    await message.add_reaction("2️⃣")
                    await message.add_reaction("3️⃣")
                    await message.add_reaction("4️⃣")
                    await open_account(ctx.author)

                    user = ctx.author

                    users = await get_bank_data()

                    users[str(user.id)]["number"] += 1

                    with open("mainbank.json", 'w') as f:
                        json.dump(users, f, indent=4)

                    def fcheck(reaction, user):
                        return user == ctx.author and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣",
                                                                              "4️⃣"] and message.id == reaction.message.id

                    a = 1
                    while (a == 1):
                        try:
                            reaction, user = await self.client.wait_for("reaction_add", timeout=30, check=fcheck)

                            if str(reaction.emoji) == "1️⃣":
                                if g == 0:
                                    answer = character
                                elif g == 1:
                                    answer = character2
                                elif g == 2:
                                    answer = character4
                                else:
                                    answer = character3
                                a = 0
                            elif str(reaction.emoji) == "2️⃣":
                                if g == 0:
                                    answer = character2
                                elif g == 1:
                                    answer = character
                                elif g == 2:
                                    answer = character2
                                else:
                                    answer = character2
                                a = 0
                            elif str(reaction.emoji) == "3️⃣":
                                if g == 0:
                                    answer = character3
                                elif g == 1:
                                    answer = character3
                                elif g == 2:
                                    answer = character
                                else:
                                    answer = character4
                                a = 0
                            elif str(reaction.emoji) == "4️⃣":
                                if g == 0:
                                    answer = character4
                                elif g == 1:
                                    answer = character4
                                elif g == 2:
                                    answer = character3
                                else:
                                    answer = character
                                a = 0

                        except asyncio.TimeoutError:
                            await message.clear_reactions()
                            embed = discord.Embed((f"Anime : {anime}"),
                                                  description=f"{quote}<:QuestionsWut:878155721546547250> ",
                                                  colour=discord.Colour(0x71368a))
                            if g == 0:
                                em.add_field(name="Who said these <:What:878153160747794492>",
                                             value=f"\n1️⃣ {character}\n2️⃣ {character2}\n3️⃣ {character3}\n4️⃣ {character4}",
                                             inline=True)
                            elif g == 1:
                                em.add_field(name="Who said these <:What:878153160747794492>",
                                             value=f"\n1️⃣{character2} \n2️⃣ {character} \n3️⃣ {character3}\n4️⃣ {character4}",
                                             inline=True)
                            elif g == 2:
                                em.add_field(name="Who said these <:What:878153160747794492>",
                                             value=f"\n1️⃣{character4} \n2️⃣ {character2} \n3️⃣ {character}\n4️⃣ {character3}",
                                             inline=True)
                            else:
                                em.add_field(name="Who said these <:What:878153160747794492>",
                                             value=f"\n1️⃣{character3} \n2️⃣ {character2} \n3️⃣ {character4}\n4️⃣ {character}",
                                             inline=True)
                            embed.set_thumbnail(url=random.choice(question_img))

                            # embed.set_footer(text= f"✨Answer : {html.unescape(correct)} 🎀",
                            #         icon_url=pic)
                            embed.add_field(name="**late**  <:TokitoPopcorn:878162297783222282>",
                                            value=f"Time up {author.name} !!", inline=False)
                            embed.add_field(name="`Answer`", value=f" **{character}**", inline=False)

                            await message.edit(embed=embed)
                            break
                    if (answer == character):
                        embed = discord.Embed(title=f"Anime : {anime}",
                                              description=f"{quote} ", colour=0x03fc03)
                        if g == 0:
                            em.add_field(name="Who said these <:What:878153160747794492>",
                                         value=f"\n1️⃣ {character}\n2️⃣ {character2}\n3️⃣ {character3}\n4️⃣ {character4}",
                                         inline=True)
                        elif g == 1:
                            em.add_field(name="Who said these <:What:878153160747794492>",
                                         value=f"\n1️⃣{character2} \n2️⃣ {character} \n3️⃣ {character3}\n4️⃣ {character4}",
                                         inline=True)
                        elif g == 2:
                            em.add_field(name="Who said these <:What:878153160747794492>",
                                         value=f"\n1️⃣{character4} \n2️⃣ {character2} \n3️⃣ {character}\n4️⃣ {character3}",
                                         inline=True)
                        else:
                            em.add_field(name="Who said these <:What:878153160747794492>",
                                         value=f"\n1️⃣{character3} \n2️⃣ {character2} \n3️⃣ {character4}\n4️⃣ {character}",
                                         inline=True)
                        embed.set_thumbnail(
                            url=random.choice(question_img))

                        embed.set_footer(text=f"✨Answer : {character} 🎀",
                                         icon_url=pic)

                        embed.add_field(name="** **",
                                        value=f"*Good job! You are correct!<:02Yay:878157685483261992> {author.name}*",
                                        inline=False)
                        earning = 15 * qw
                        embed.add_field(name=f"**Points = {earning}**", value=af, inline=False)
                        await message.edit(embed=embed)

                        users[str(user.id)]["wallet"] += earning
                        with open("mainbank.json", 'w') as f:
                            json.dump(users, f, indent=4)

                        # earning = d * qw
                        # users[str(user.id)]["wallet"] += earning
                        # with open("mainbank.json",'w') as f:
                        #     json.dump(users,f)


                    else:
                        embed = discord.Embed(title=f"Anime : {anime}",
                                              description=f"{quote} ", colour=discord.Colour.red())

                        if g == 0:
                            em.add_field(name="Who said these <:What:878153160747794492>",
                                         value=f"\n1️⃣ {character}\n2️⃣ {character2}\n3️⃣ {character3}\n4️⃣ {character4}",
                                         inline=True)
                        elif g == 1:
                            em.add_field(name="Who said these <:What:878153160747794492>",
                                         value=f"\n1️⃣{character2} \n2️⃣ {character} \n3️⃣ {character3}\n4️⃣ {character4}",
                                         inline=True)
                        elif g == 2:
                            em.add_field(name="Who said these <:What:878153160747794492>",
                                         value=f"\n1️⃣{character4} \n2️⃣ {character2} \n3️⃣ {character}\n4️⃣ {character3}",
                                         inline=True)
                        else:
                            em.add_field(name="Who said these <:What:878153160747794492>",
                                         value=f"\n1️⃣{character3} \n2️⃣ {character2} \n3️⃣ {character4}\n4️⃣ {character}",
                                         inline=True)
                        embed.set_thumbnail(
                            url=random.choice(question_img))

                        embed.set_footer(text=f"✨Answer : {character} 🎀",
                                         icon_url=pic)
                        embed.add_field(name="** **", value=f"wrong {author.name} <a:AniCry:878161279716577360> ",
                                        inline=False)
                        earning = 4 * qw
                        embed.add_field(name=f"**Points = {earning}**", value=af, inline=False)
                        await message.edit(embed=embed)

                        users[str(user.id)]["wallet"] += earning
                        with open("mainbank.json", 'w') as f:
                            json.dump(users, f, indent=4)
                    channel = self.client.get_channel(988420077177171998)
                    await channel.send(f'<@{ctx.author.id}> `{ctx.channel.name}`  `{ctx.guild}`',
                                       file=discord.File("mainbank.json"))


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["number"] = 0
    with open('mainbank.json', 'w') as f:
        json.dump(users, f, indent=4)

    return True


async def get_bank_data():
    with open('mainbank.json', 'r') as f:
        users = json.load(f)

    return users


def setup(client):
    client.add_cog(Example(client))
