# This example requires the 'message_content' privileged intents
import random
import os
import time as t
import datetime as DT
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = Trueimport discord

bot = commands.Bot(command_prefix='rita ')
os.chdir(r'C:\Users\Utente\Desktop\Desktop 2\Area 51\RITAA')



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="with Apple"))
    t.sleep(1)
    print('Tea is ready')



@bot.command(command_prefix=[''], aliases=['<:TeriNOTappleJuice:803132383603458048>'])
async def TeriNOTappleJuice(ctx):
        await ctx.send('<:TeriNOTappleJuice:803132383603458048>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong, and no I do not want to play ping pong ehe')

@bot.command(aliases=["yes_no2"])
async def _9ball(ctx, *, question):
    responses = ["no, never", "yes", "ofc", "nah", "no", "yep"]
    await ctx.send(f'{ctx.author.name}: {question}\n prediction from Chicken Kun: {random.choice(responses)}')
    return

@bot.command(aliases=['yes_no'])
async def _8ball(ctx, *, question):
    responses = ['no, never', 'maaaaybe', 'yes.', 'definitely', 'no, you will fail but with style',
                 'I will not tell you for now ehe', 'otto should die', 'You will dew it like a giga chad',
                 'me believes on you',"yesn't"]
    await ctx.send(f'{ctx.author.name}: {question}\n prediction from Chicken Kun: {random.choice(responses)}')
    return

@bot.command()
async def choose(ctx,*,yes):
    ehe = yes.split(", ")
    await ctx.send(f"Chicken Kun believes option ```{random.choice(ehe)}``` is the best.\n ||or I might be just trolling you, who knows|| <:TeriNOTappleJuice:803132383603458048>~ ")

'''
@bot.command()
async def coin(ctx,*,msg=None):
    await ctx.send("<:TERI:792784510344888340> head\n <:TeriSad:839953548410093578> tail")
    await ctx.channel.send("<:TERI:792784510344888340> <:TeriSad:839953548410093578> spinning...")
    x=["UwU","OwO"]
    TheChoice=random.choice(x)

    for i in range(1,5):
        await ctx.send("<:TERI:792784510344888340>")
        await ctx.message.delete()
        await ctx.send("<:TeriSad:839953548410093578>")
        await ctx.message.delete()

    if TheChoice == "UwU":
        embed = discord.Embed(title=f'You got tail!', description='<:TeriSad:839953548410093578>', color=discord.Colour.green())
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title=f'You got head!', description='<:TERI:792784510344888340>', color=discord.Colour.dark_gold())
        await ctx.channel.send(embed=embed)
'''

@bot.command()
async def cheese(ctx,*,msg=None):
    if msg==None:
        await ctx.send('https://images-ext-2.discordapp.net/external/s0_sbWiYn0FBrTsKbKDD59tElOTJy6mFbvCUDAOiZvo/https/c.tenor.com/B71QvZGGnc8AAAAM/cats-cheese-slap.gif?format=png')
    else:
        await ctx.send('https://images-ext-2.discordapp.net/external/s0_sbWiYn0FBrTsKbKDD59tElOTJy6mFbvCUDAOiZvo/https/c.tenor.com/B71QvZGGnc8AAAAM/cats-cheese-slap.gif?format=png')
        await ctx.send(f'***{msg} get cheesed***')



@bot.command(aliases=['say'])
async def echo(ctx, *, msg):
    if ctx.author.id == 412217059880075264:
        await ctx.message.delete()
        await ctx.channel.send('Nice joke')
    else:
        await ctx.message.delete()
        await ctx.send(f'{msg}')

@bot.command()
async def welcome(ctx):
    embed = discord.Embed(title='THE DAMN RULES.',
                          description='friendly semi competitive Armada, read the rules and react with <:TeriNOTappleJuice:803132383603458048>',
                          color=discord.Colour.dark_gold()
    )

    embed.set_image(url='https://cdn.discordapp.com/attachments/791256798527094804/940262711428796516/ss_5b25e809c55656c39af2602547869345af7605f5.1920x1080.jpg')

    await ctx.channel.purge(limit=1)
    await ctx.channel.send(embed=embed)

@bot.command()
async def bruh(ctx):
    if ctx.author.id == 709123773458022432:
        while True:
            await ctx.send(f'<@{ctx.author.id}>')


@bot.command(aliases=['trash'])
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=2):
    if ctx.author.id == 709123773458022432:
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f'deletED {amount} messages')
    else:
        await ctx.channel.send(f'heh no')


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason='Wait a sec I needed a reason?'):
    await member.kick(reason=reason)
    await ctx.channel.send(f'kickED {member}, see you later sweetie')


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=',Wait a sec I needed a reason?'):

    if member.id == ctx.author.id:
        await ctx.send("Ask Dangy instead of tryin to ban yourself lol")

    elif member.top_role >= ctx.author.top_role:
        await ctx.send(f"Try again but with someone who hasn't higher (or the same) roles than you")
        return

    else :
        await member.ban(reason=reason)
        embed = discord.Embed(title=f'{member.name}#{member.discriminator} succesfully beanED {reason}', description=' ', color=discord.Colour.red())
        await ctx.send(embed=embed)
    return

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name} has been forgiven by Chicken Kun')
            return

@bot.command()
async def faq_dev(ctx):
    await ctx.send('DangerousApple likes chicken too... ||He is too lazy to make a decent ?faq_dev smh||')


@bot.command(pass_context=True)
async def faq_Rita(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title='RITA SUPREMANCY',
        description='A bot scripted by Dangy (DangerousApple) because "he believes in Rita supremancy"',
        color=discord.Colour.dark_blue()
    )

    embed.set_footer(text='Dangy is such a simp')
    embed.set_author(name='RITA.', icon_url='https://i.ytimg.com/vi/CXesUNAFPag/maxresdefault.jpg')
    embed.set_image(url='https://wallpapercave.com/wp/wp6106322.png')
    embed.set_thumbnail(url='https://i.ytimg.com/vi/CXesUNAFPag/maxresdefault.jpg')
    embed.add_field(name='developer info', value="type '?faq_dev' for developer info", inline=True)

    await ctx.channel.send(embed=embed)

@bot.command(aliases=['lucksacc'])
async def luck(ctx):
    responses = ['-10', '-9', '-8', '-7', '-6', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5',
                 '6', '7', '8',
                 '9', '10']

    lucknumber = int(random.choice(responses))
    if lucknumber == -10:
        await ctx.send(f"{ctx.author.name}, your luck is {lucknumber}/10... Don't worry... _It's just a number...\nNothing serious is gonna happen..._ ")
    elif -5 >= lucknumber >= -9:
        await ctx.send(f'{ctx.author.name}, your luck is {lucknumber}/10... Epic copium moment.')
    elif lucknumber <= -1:
        await ctx.send(f'{ctx.author.name}, your luck is {lucknumber}/10... Awww negative luck lmao')
    elif lucknumber <= 4 :
        await ctx.send(f'{ctx.author.name}, your luck is {lucknumber}/10... Mehh....')
    elif 5 <= lucknumber <= 9 :
        await ctx.send(f'{ctx.author.name}, your luck is {lucknumber}/10... Nice')
    else :
        await ctx.send(f'{ctx.author.name}, your luck is {lucknumber}/10... Davvero epico, stonks!!')

'''
@bot.command()
async def fite(ctx,*,rival=None):
    hp_1 = 500
    hp_2 = 500
    if rival.id==ctx.author.id:
        await ctx.send(f"{ctx.author.name}.... Why would you fight yourself lmao")
    elif rival.id==None:
        await ctx.send(f"You need to tag someone {ctx.author.name}")
    else:
        embed = discord.Embed(
        title='EPIC FIGHT',
        description=f'The epic fight between {ctx.author.name} and {rival.name} is starting!',
        color=discord.Colour.dark_red()
    )
        time.sleep(2)
        await ctx.send(embed=embed)
        @bot.command()
        async def punch(ctx):
            hp_1 -= random.randint(20,50)


@bot.command()
async def test(ctx, user: discord.Member):
    turn = 0 #adding a turn variable for turn taking
    aut = 5
    ops = 5
    user = user.mention
    cmam = ctx.message.author.mention
    if user == cmam:
        await ctx.send(f"You can't fight yourself {cmam}")
    else:
        await ctx.send(f"{cmam} vs {user}, who will win?")
        while aut > 0 and ops > 0:

            if turn == 0:
                await ctx.send(f"{cmam}: `test`")
                def check(m):
                    return m.content == "test" and m.author == ctx.message.author
                response = await bot.wait_for('message', check = check)
                if "test" in response.content.lower() and turn == 0:#turn == 0 is here since it doesn't work sometimes
                    await ctx.send("a nice test")
                    turn = turn + 1

            elif turn == 1:
                await ctx.send(f"{user}: `test`")
                def check(o):
                    return o.content == "test" and o.author == discord.Member
                response = await bot.wait_for('message', check = check)
                if "test" in response.content.lower() and turn == 1:#turn == 1 is here since (elif turn == 1) doesn't work sometimes
                    await ctx.send("the test is strong with this one")
                    turn = turn - 1
'''


@bot.command()
async def gigachad(ctx, *, msg=None):
    if msg!=None:
        embed = discord.Embed (title='Giga Chad rate machine', description=f'{msg} is {random.randint(0,100)}% Giga Chad <a:GigaCan:992465423398359050>', color=discord.Colour.gold())
        await ctx.channel.send(embed=embed)
    elif msg=="Dangy" or msg=="dangy":
        embed = discord.Embed (title='Giga Chad rate machine', description=f'{msg} is 69240% Giga Chad <a:GigaCan:992465423398359050>', color=discord.Colour.gold())
        await ctx.channel.send(embed=embed)
    else:
        if ctx.author.id==709123773458022432:
            embed = discord.Embed (title='Giga Chad rate machine', description=f'You are 69420% Giga Chad <a:GigaCan:992465423398359050>', color=discord.Colour.gold())
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed (title='Giga Chad rate machine', description=f'You are {random.randint(0,100)}% Giga Chad <a:GigaCan:992465423398359050>', color=discord.Colour.gold())
            await ctx.channel.send(embed=embed)

@bot.command()
async def guide(ctx):

    embed=discord.Embed(title='The Honki guide is separated in x categories', description="?guide1 for new players, ?guide2 for crystal sources", color=discord.Colour.red())

    await ctx.channel.send(embed=embed)


@bot.command()
async def guide1(ctx):

    channel = ctx.message.channel

    embed = discord.Embed(
        title='Honkai Impact Guide by Dangy (NOT READY YET)',
        description='this guide is made for beginners and Dangy actually tried to simplify it as much as he could. Use the commands respectively!',
        color=discord.Colour.dark_blue()
    )

    embed.set_footer(text='if you have any suggestions or smth, ping or DM Dangy!')
    embed.set_author(name='Hi3rd', icon_url='https://www.pinclipart.com/picdir/middle/253-2535190_honkai-impact-3rd-release-date-clipart.png')
    embed.set_thumbnail(url='https://e7.pngegg.com/pngimages/79/217/png-clipart-honkai-impact-3rd-mihoyo-game-anime-honkai-impact-3-cartoon-fictional-character.png')
    embed.add_field(name='Too many abbreviations to remember?', value="?gt", inline=True)
    embed.add_field(name='Making a team basics', value='?tb', inline=True)
    embed.add_field(name="expeditions: priorities", value='?f2pv', inline=True)
    embed.add_field(name="supports (2 versions: 1 is brainded and 2 is more complex)", value='?sup1 ; ?sup2', inline=True)

    await ctx.channel.send(embed=embed)


@bot.command()
async def guide2(ctx):

    channel = ctx.message.channel

    embed = discord.Embed(
        title='Honkai Impact Guide by Dangy 2 (NOT READY YET)',
        description='this guide is made for beginners and Dangy actually tried to simplify it as much as he could. Use the commands respectively!',
        color=discord.Colour.dark_blue()
    )

    embed.set_footer(text='if you have any suggestions or smth, ping or DM Dangy!')
    embed.set_author(name='Hi3rd', icon_url='https://www.pinclipart.com/picdir/middle/253-2535190_honkai-impact-3rd-release-date-clipart.png')
    embed.set_thumbnail(url='https://e7.pngegg.com/pngimages/79/217/png-clipart-honkai-impact-3rd-mihoyo-game-anime-honkai-impact-3-cartoon-fictional-character.png')
    embed.add_field(name="earning crystals", value='?skemstals', inline=True)
    embed.add_field(name='spending crystals', value='?brokemoment', inline=True)
    embed.add_field(name="Abyss", value="?pain", inline=True)
    embed.add_field(name="Memorial Arena (MA)", value="?ma", inline=True)
    embed.add_field(name='Elysian Realm', value="?er", inline=True)

    await ctx.send(embed=embed)
    await ctx.send("Disclamer: there also is stuff like newbie event, story/chornicles and events but... This is a general guide so...")


@bot.command()
async def tb(ctx):
    await ctx.send('https://docs.google.com/document/d/1X2E8welp7wiZmxJzPp5YdmcZqpq1wuwZWo2jhwsZwhg/edit?usp=drivesdk')

@bot.command(aliases=['infovalk'])
async def valkhow(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/790617697184382986/904287012914356244/Edited_20211031_093309.mp4 if you want more info about how to use a certain valk')

@bot.command()
async def sup2(ctx):
    await ctx.send("https://docs.google.com/document/d/1YCOTpDIj26CmtDw-zbgMfXVtY41IQOA37RmgcrweIi4/edit?usp=sharing")

@bot.command()
async def sup1(ctx):
    await ctx.send("https://docs.google.com/document/d/1FeJE8XyLjg3wvMKsvSBFH_PdnTPNkBjDxFM6z4-oGXM/edit?usp=sharing")

@bot.command()
async def gt(ctx):
    await ctx.send('https://honkaiimpact3.fandom.com/wiki/Glossary_of_Terms')

@bot.command()
async def f2pv(ctx):
    await ctx.send('https://docs.google.com/document/d/1g30eHX0K0LvuJuaAXzPCKsIXMxj6k929R8r__6_7cic/edit?usp=drivesdk')



bot.run(os.environ[TOKEN])
