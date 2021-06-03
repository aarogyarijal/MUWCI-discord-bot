# bot.py
import discord
from discord.ext import commands, tasks
from discord import ChannelType
import asyncio
from itertools import cycle
import time
from random import randint, choice
import api

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents)
status = cycle(["Lord Big Rogi", ".usage for help", "baby shark"])

pps = ["has 2 pp", "is pregnant", "has a bhery smol pp","has no pp","has enormousley smol pp."]
maxpp = len(pps)



@client.event
async def on_ready():
    change_status.start()
    print(f'{client.user} has connected to Discord!')

@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=(next(status))))

@client.command()
async def usage(ctx):
    myid='<@299776649673703424>'
    await ctx.send(f"""**Hi there!**
**The command prefix for the bot is ' . ' meaning that all commands start with a period.**
    
To start the **Speed Dating Channel Hider**:
Type `.sd` *Make sure you run this command when the channel is empty or this will not work.*

To **roast somebody**:
Type `.roast <user_to_roast>`

To **compliment somebody**:
Type `.comp <username>`

To **get a pun**:
Type `.pun`

To **get a joke**:
Type `.joke`

To **get a Dad Joke**:
Type `.dad`

To **find the size of someones pp**:
Type `.pp <username>`

To **get a dog pic**:
Type `.doggo <optional:breed>`


**APIs used in this bot:**
1) <https://sv443.net/jokeapi/v2/joke>
2) <https://evilinsult.com/>
3) <https://complimentr.com>
4) <https://dog.ceo>

**Bot is now hosted online at <https://heroku.com>**

If the bot is not working or if you have any additional ideas, feel free to contact me.

-{myid}""", embed=None)

@client.command()
async def roast(ctx, name=""):
    roast = api.get_roast()
    if roast == False:
        await ctx.send("Couldn't get joke from API. Try again later.")
    else:
        if (name == "<@!299776649673703424>"):
            await ctx.send(f'{name} is a good boy')
        else:
            await ctx.send(f'{name} {roast["insult"]}')

@client.command()
async def comp(ctx, name=""):
    comp = api.get_comp()
    if comp == False:
        await ctx.send("Couldn't get compliment from API. Try again later.")
    else:
        await ctx.send(f'{name}, {comp["compliment"]}')

@client.command()
async def joke(ctx):
    joke = api.get_joke()
    if joke == False:
        await ctx.send("Couldn't get joke from API. Try again later.")
    else:
        await ctx.send(joke['joke'])

@client.command()
async def pun(ctx):
    pun = api.get_pun()
    if pun == False:
        await ctx.send("Couldn't get pun from API. Try again later.")
    else:
        await ctx.send(pun['setup'])
        await asyncio.sleep(5)
        await ctx.send(pun['delivery'])

@client.command()
async def pp(ctx, name=""):
    chosen = randint(0,maxpp-1)
    if (name == ""):
        while True:
            members = ctx.message.channel.members
            name = choice(members)
            if (name.bot==False):
                await ctx.send(f'{name.mention} {pps[chosen]}')
                break
    elif (name == "<@!299776649673703424>"):
        await ctx.send(f'{name} has bhery big pp')
    else:
        await ctx.send(f'{name} {pps[chosen]}')

@client.command(aliases=["kutta", "kutha"])
async def doggo(ctx, breed=""):
    dog = api.get_dog(breed)
    if dog == False:
        await ctx.send("Couldn't get pun from API. Try again later.")
    else:
        await ctx.send(dog['message'])

@client.command(aliases=["billi","billa", "meow"])
async def cat(ctx):
    cat = api.get_cat()
    if cat == False:
        await ctx.send("Couldn't get pun from API. Try again later.")
    else:
        await ctx.send(cat[0]['url'])

@client.command()
async def dad(ctx):
    dad = api.get_dad()
    print(dad)
    if dad == False:
        await ctx.send("Couldn't get pun from API. Try again later.")
    else:
        await ctx.send(dad['joke'])


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command(pass_context=True)
async def sd(ctx):
    myid='<@299776649673703424>'
    await ctx.send(f"Speed Dating Channel Hider is running! -{myid}")
    channel1 = client.get_channel(758013927950123208)
    channel2 = client.get_channel(758014182032408608)
    everyone = ctx.guild.default_role
    while True:
        # gets the channel you want to get the list from
        members1 = channel1.members
        members2 = channel2.members
        counter1 = len(members1)
        counter2 = len(members2)
        localtime = time.asctime( time.localtime(time.time()) )
        print(f'{localtime} -- Counter: {counter1}, {counter2}')
        if counter1 >= 2:
            await channel1.set_permissions(everyone, view_channel=False)
        else:
            await channel1.set_permissions(everyone, view_channel=True)
        if counter2 >= 2:
            await channel2.set_permissions(everyone, view_channel=False)
        else:
            await channel2.set_permissions(everyone, view_channel=True)

#testing codes
# @client.command()
# async def findvc(ctx, name):
#     # find a guild by name
#     guild = discord.utils.get(client.guilds, name="Social Center")
#     # make sure to check if it's found
#     if guild is not None:
#         # find a channel by name
#         channel = discord.utils.get(guild.voice_channels, name=name)
#     await ctx.send(channel.id)

# @client.command()
# async def test(ctx, user):
#     print(user)

# @client.command()
# async def mem(ctx):
#     channel1 = client.get_channel(758013927950123208)
#     channel2 = client.get_channel(758014182032408608)
#     members1 = channel1.members
#     members2 = channel2.members
#     print(channel1, channel2)
#     print(members1, members2)
client.run('xxxxxxxxxxxxx')

