# bot.py
import discord
from discord.ext import commands
from discord import ChannelType
import asyncio
from itertools import cycle
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents)
import time
from random import randint, choice



insults = [
"I'd like to roast you, but it looks like God already did.",
"You look like someone set your face on fire and then put it out with a hammer.",
"The only thing attracted to you is gravity",
"You’re not good looking enough to be a model, but you’re not smart enough to be anything else",
"If you’d like to know what sexual position produces the ugliest babies, you should ask your mother.",
"Can you speak a little louder? I can’t hear you over the sound of how stupid you are.",
"Why are you even talking to me? So your self esteem can match your IQ?",
"I’m not insulting you, I’m describing you.",
"If you hide your big nose and shut your big mouth, people will think you are attractive and well-spoken.",
"I guess God’s just making anybody these days.",
"You're so ugly, when your mom dropped you off at school she got a fine for littering.",
"Some babies were dropped on their heads but you were clearly thrown at a wall.",
"They say opposites attract. If that's so, you will meet someone who is good-looking, intelligent, and cultured.",
"I didn’t hear you. I’m busy ignoring an annoying person.",
"I don't know what your problem is, but I'll bet it's hard to pronounce.",
"Please excuse me while I transfer you to someone who speaks Fucktard.",
"It must take a lot of flexibility to fit your foot in your mouth and your head up your ass at the same time.",
"I don’t have the time nor the crayons to explain things to you",
"I’d love to keep chatting with you, but I’d rather have AIDS",
"I bet you swim with a t shirt on",
"You have all the charm and charisma of a burning orphanage",
"Your face is so oily that I’m surprised America hasn’t invaded yet.",
"If you were any dumber, someone would need to water you twice a week",
"If you were on fire and I had a cup of my own piss, I’d drink it",
"Do you still love nature, despite what it did to you?",
"The thing I dislike most about your face is that I can see it.",
"If B.S. was music, you’d be an orchestra.",
"You look like a before picture.",
"I’ve heard farts more intelligent than you.",
"You have a perfect face for radio.",
"They say that a million monkeys on a million typewriters will eventually produce the collected works of Shakespeare. If that theory is correct, I believe you will one day say something intelligent.",
"If you want to lose ten pounds of ugly fat, may I suggest you start with cutting off your head.",
"You look like somebody stepped on a goldfish.",
"I thought the trash got picked up last night, what are you still doing here?",
"Looking the way you do must save a lot of money on halloween.",
"I’d love to continue talking with you but my favorite commercial is on tv",
"I'd love to keep chatting with you, but right now I have to do literally anything else.",
"Did you get a bowl of soup with that haircut?",
"If you don’t like what I say about you, it would be a good idea to improve yourself.",
"Does being that ugly require a license?",
"You could throw a rock at the ground and miss",
"There’s no one in this world like you. Or at least I hope so.",
"You look like a man, and you need to lose some weight.",
"Did you cancel your barbecue?  Because your grill is messed up",
"Some people make millions.  You make memes.",
"Did you forget to wipe or is that your natural scent?",
"I missed you this week, but my aim is improving.",
"I'm surprised you've made it this far without being eaten.",
"Your body looks like your head is inflating a water balloon.",
"Your mother was a hamster.",
"How do you make an idiot wait?",
"If balls were dynamite, you wouldn't have enough to kill a fish.",
"I'd like to roast you, but I'm too busy judging your choices.",
"You are the worst part of everybody's day.",
"If your face were scrambled it would improve your looks.",
"I hope you don't feel the way you look.",
"In the book of Who's Who, you are listed as What's That?",
"It's surprising to me that a pig's bladder on a stick has gotten so far in life.",
"Sorry.  I'm on the toilet and I can only deal with one shit at a time.",
"If you fell into a river it would be unfortunate, but if anyone pulled you out it would be a disaster.",
"You are the discount version of whatever celebrity you look like.",
"When you go to the dentist, he needs anaesthetic.",
"You suck dick for bus fare and then walk home.",
"The fact that you are still alive is evidence that natural disasters are poorly distributed.",
"You are so dumb you can't fart and chew gum at the same time.",
"I was going to give you a nasty look, but I see you already have one.",
"Me think'st thou are a general offence and every man should beat thee.",
"I don't try to explain myself to idiots like you.  I'm not the Fucktard Whisperer.",
"Your mom circulates like a public key, servicing more requests than HTTP.",
"Your mom is so fat and dumb, the only reason she opened her email is because she heard it contained spam.",
"Your mom is so fat, she has to iron her pants in the driveway.",
"Your face invites a slap.",
"The only way you could get laid is if you crawled up a chicken's ass and waited."
'One time I masturbated on a plane.I called it "highjacking"'
]

puns = [
  {
    "pun": "Q: How many programmers does it take to change a light bulb?",
    "punchline": "A: None. It's a hardware problem!"
  },
  {
    "pun": "Q: What does a proud computer call its little son?",
    "punchline": "A: A microchip off the old block!"
  },
  {
    "pun": "Q: What is another name for a computer virus?",
    "punchline": "A: A terminal illness!"
  },
  {
    "pun": "Q: Why did the computer spy quit?",
    "punchline": "A: They couldn’t hack it anymore!"
  },
  {
    "pun": "Q: What did the motherboard say to the new software?",
    "punchline": "A: I'll show you who's Dos!"
  },
  {
    "pun": "Q: What does a floppy disk do when it needs a break?",
    "punchline": "A: It goes for a C: drive!"
  },
  {
    "pun": "Q: Why was the computer geek disappointed by the zoo?",
    "punchline": "A: They couldn't find any RAM!"
  },
  {
    "pun": "Q: Which way did the computer programmer go?",
    "punchline": "A: They went data way!"
  },
  {
    "pun": "Q: What do you get when you cross a computer with a hamburger?",
    "punchline": "A: A Big Mac!"
  },
  {
    "pun": "Q: How do you find a spider on the internet?",
    "punchline": "A: Check out its web site!"
  },
  {
    "pun": "Q: How did the computer catch a cold?",
    "punchline": "A: Someone opened too many Windows!"
  },
  {
    "pun": "Q: Why don't Vikings like to send emails?",
    "punchline": "A: They prefer to use Norse code!"
  },
  {
    "pun": "Q: What do you say when a JavaScript interview went bad?",
    "punchline": "A: Don't call us, we'll callback you. We promise!"
  },
  {
    "pun": "Q: Why did the computer programmer drown?",
    "punchline": "A: They couldn't figure out whether to float left or right!"
  },
  {
    "pun": "Q: How do you comfort a JavaScript bug?",
    "punchline": "A: You console it!"
  },
  {
    "pun": "Q: Why did the programmer quit their job?",
    "punchline": "A: Because they didn't get arrays!"
  },
  {
    "pun": "Q: What do computers and air conditioners have in common?",
    "punchline": "A: They both become useless when you open Windows!"
  },
  {
    "pun": "Q: Why do Java programmers wear glasses?",
    "punchline": "A: They cannot C#!"
  },
  {
    "pun": "Q: Do you know the band 1023 megabytes?",
    "punchline": "A: They haven't had a gig yet!"
  },
  {
    "pun": "Q: Why was the database admin kicked out of the bar?",
    "punchline": "A: They kept joining the tables."
  },
  {
    "pun": "Q: Why did the JavaScript developer lose their job?",
    "punchline": "A: They couldn't keep their Promises!"
  },
  {
    "pun": "Q: Did you hear about the monkeys who shared an Amazon account?",
    "punchline": "A: They were Prime mates!"
  },
  {
    "pun": "Q: What are computers' favorite snacks?",
    "punchline": "A: Microchips, phish sticks, and cookies. But just a few bytes of each!"
  },
  {
    "pun": "Q: Why was the network administrator late to work?",
    "punchline": "A: There was lots of traffic congestion and even a collision. Everything was backed up. It was a hard drive!"
  },
  {
    "pun": "Q: What wedding gift should you buy for a Windows administrator?",
    "punchline": "A: I don't know. Perhaps you should check the registry for clues!"
  },
  {
    "pun": "Q: Where's the best place to hide a body?",
    "punchline": "A: Page two of Google!"
  },
  {
    "pun": "Q: What is the biggest lie in the entire universe?",
    "punchline": "A: 'I have read and agree to the Terms & Conditions.'"
  },
  {
    "pun": "Q: What do computers do on a beach vacation?",
    "punchline": "A: Surf the net!"
  },
  {
    "pun": "Q: Why are people afraid of computers?",
    "punchline": "A: They byte!"
  },
  {
    "pun": "Q: Why do people on Twitter tell me I'm always confused?",
    "punchline": "A: Because I don't follow!"
  },
  {
    "pun": "Q: How does a computer get drunk?",
    "punchline": "A: It takes screenshots!"
  },
  {
    "pun": "Q: Why do app developer's have such high insurance rates?",
    "punchline": "A: They're always crashing!"
  },
  {
    "pun": "Q: Why doesn't the developer use Git?",
    "punchline": "A: Because they're afraid to commit!"
  },
  {
    "pun": "Q: Why does a front end developer eat alone?",
    "punchline": "A: Because they don't know how to join the tables!"
  },
  {
    "pun": "Q: Did you hear about the Linux sysadmin who won Strictly?",
    "punchline": "A: They really came out of their shell!"
  },
  {
    "pun": "Q: Why are Java programmers front yards so untidy?",
    "punchline": "A: Because they are always waiting on garbage collection!"
  },
  {
    "pun": "Q: What do you call a Rails developer?",
    "punchline": "A: A conductor!"
  },
  {
    "pun": "Q: Where do naughty disk drives get sent?",
    "punchline": "A: Boot camp!"
  },
  {
    "pun": "Q: What do you call it when you have your mom's mom on speed dial?",
    "punchline": "A: Instagram!"
  },
  {
    "pun": "Q: Why did the functions stop calling each other?",
    "punchline": "A: Because they had constant arguments!"
  },
  {
    "pun": "Q: What's the most cutting edge language?",
    "punchline": "A: C#!"
  },
  {
    "pun": "Q: Why couldn't the programmer dance to the song?",
    "punchline": "A: Because they didn't get the algo-rhythm!"
  },
  {
    "pun": "Q: Why do universities hate Java programmers?",
    "punchline": "A: They're always starting public classes!"
  },
  {
    "pun": "Q: Why are programmers popular on the street?",
    "punchline": "A: They'll write scripts for anything at the right price!"
  },
  {
    "pun": "Q: Why is everyone who works at the keyboard factory so rich?",
    "punchline": "A: They put in a lot of shifts!"
  },
  {
    "pun": "Q: Why don't programmers like nature?",
    "punchline": "A: Too many bugs!"
  },
  {
    "pun": "Q: How many bits of bait does a programmer need to go fishing?",
    "punchline": "A: At least 8, or else the fish won't byte!"
  },
  {
    "pun": "Q: Why were the Javascript plumbers delayed?",
    "punchline": "A: Because they had to await async!"
  },
  {
    "pun": "Q: Why was the IT engineer in the hospital?",
    "punchline": "A: They touched the firewall!"
  },
  {
    "pun": "Q: How do you generate a random string?",
    "punchline": "A: Put a Windows user in front of vim and tell them to exit!"
  },
  {
    "pun": "Q: How many testers does it take to change a light bulb?",
    "punchline": "A: None. Testers do not fix problems; they just report them!"
  },
  {
    "pun": "Q: How many programmers does it take to change a light bulb?",
    "punchline": "A: What's the problem? The bulb at my desk works just fine!"
  },
  {
    "pun": "Q: Why did the programmer stop using Python?",
    "punchline": "A: Because they are scared of snakes!"
  },
  {
    "pun": "Q: Why did the PowerPoint Presentation cross the road?",
    "punchline": "A: To get to the other slide!"
  },
  {
    "pun": "Q: What sits on your shoulder and says 'Pieces of 7! Pieces of 7!'?",
    "punchline": "A: A Parroty Error!"
  },
  {
    "pun": "Q: Why are database admins afraid of having dinner?",
    "punchline": "A: Because the table is cleared!"
  },
  {
    "pun": "Q: Who is a computer's favorite singer?",
    "punchline": "A: A Dell!"
  },
  {
    "pun": "Q: Why did the integer never get any radio play?",
    "punchline": "A: Because it was unsigned!"
  },
  {
    "pun": "Q: How does the JavaScript function travel?",
    "punchline": "A: It fly's first-class!"
  },
  {
    "pun": "Q: What is a computer's favorite instrument?",
    "punchline": "A: The keyboard!"
  },
  {
    "pun": "Q: What does the hacker say to their mom when they're hacking people?",
    "punchline": "A: Gone Phishing!"
  },
  {
    "pun": "Q: What do Linux users wear?",
    "punchline": "A: Tux-edos!"
  },
  {
    "pun": "Q: What do you call a program whose file you can't find?",
    "punchline": "A: Soft-where!"
  },
  {
    "pun": "Q: What grade did the programmer get on their test?",
    "punchline": "A: C++!"
  },
  {
    "pun": "Q: What made the technician win the golf tournament?",
    "punchline": "A: They had a hard-drive!"
  },
  {
    "pun": "Q: Why do programmers take so long in the shower?",
    "punchline": "A: The instructions on the shampoo are: lather, rinse, repeat!"
  },
  {
    "pun": "Q: What search algorithm did the wise men use to find the baby Jesus?",
    "punchline": "A: A*"
  },
  {
    "pun": "Q: Who is mongoDB's favourite singer?",
    "punchline": "A: JSON derulo"
  },
  {
    "pun": "Q: Why was the JavaScript developer sad?",
    "punchline": "A: Because they didn't Node how to Express themselves!"
  },
  {
    "pun": "Q: Hey officer! How did the hackers escape?",
    "punchline": "A: No idea. They just ransomware."
  },
  {
    "pun": "Q: What accommodations did the JavaScript developer request at the hotel?",
    "punchline": "A: A room with a Vue."
  },
  {
    "pun": "Q: What did the router say to the doctor?",
    "punchline": "A: It hurts when IP"
  },
  {
    "pun": "Q: What do you call the top of a function that's async?",
    "punchline": "A: Tap water..."
  },
  {
    "pun": "Q: What's a pirate's favorite programming language?",
    "punchline": "A: You'd think it was R, but their first love is the C."
  },
  {
    "pun": "Q: What is the way of object oriented to become wealthy?",
    "punchline": "A: Inheritance"
  },
  {
    "pun": "Q: What is an algorithm?",
    "punchline": "A: Word used by programmers when they did not want to explain what they did"
  },
  {
    "pun": "Q: What is a programmer's favourite hangout place?",
    "punchline": "A: Foo Bar"
  },
  {
    "pun": "Q: What does a programmer say after a road trip across California?",
    "punchline": "A: It was a solid state drive"
  },
  {
    "pun": "Q: What do Javascript programmers like to order at the coffeeshop?",
    "punchline": "A: Mocha, Chai and a cup of Expresso"
  },
  {
    "pun": "Q: Which planet in the solar system would a python developer first travel to?",
    "punchline": "A: Jupyter"
  },
  {
    "pun": "Q: How did the lecturer encouraged the computer science students?",
    "punchline": "A: Git job. Git pushing on!"
  },
  {
    "pun": "Q: Which exhibition at the zoo did the python developer visit first?",
    "punchline": "A: The Anaconda"
  },
  {
    "pun": "Q: Why did a couple of programmers go to the farmer’s market?",
    "punchline": "A: They went there to do pear programming"
  },
  {
    "pun": "Q: Did you hear about the programmer who spent a day walking round in circles?",
    "punchline": "A: After a while they really needed a break"
  },
  {
    "pun": "Q: Did you hear about X's and Y's wedding? There were 10 arguments!",
    "punchline": "A: Well, it was a very large function!"
  },
  {
    "pun": "Q: Why was the cell phone wearing glasses?",
    "punchline": "A: It lost its contacts!"
  },
  {
    "pun": "Q: What’s an alien favorite key?",
    "punchline": "A: The space bar!"
  },
  {
    "pun": "Q: What do you call a programmer who acts in a strange way?",
    "punchline": "A: A programmer with undefined behaviour"
  },
  {
    "pun": "Q: What do some programmers call their Grandmas?",
    "punchline": "NaN"
  },
  {
    "pun": "Q: Why won't they let the programmer write any loops with iterators?",
    "punchline": "A: Because the programmer is called is Obi-Wan"
  },
  {
    "pun": "Q: What did the programmer say when they couldn't debug their code?",
    "punchline": "A: It's imparsable"
  },
  {
    "pun": "Q: What do programmers do when they're hungry?",
    "punchline": "A: They grab a byte"
  },
  {
    "pun": "Q: What do you call a group of 8 hobbits?",
    "punchline": "A: A hobbyte"
  }
]

pps = ["has a bhery smol pp","has no pp","has enormousley smol pp."]

max = len(insults)
maxp = len(puns)
maxpp = len(pps)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Lord Big Rogi"))
    print(f'{client.user} has connected to Discord!')
    
@client.command()
async def roast(ctx, name=""):
    # if (name == ""):
    #     channel = message.channel
    #     name = random.choice(channel.guild.members)
    chosen = randint(0,max-1)
    await ctx.send(f'{name} {insults[chosen]}')

@client.command()
async def pp(ctx, name=""):
    if (name == ""):
        while True:
            members = ctx.message.channel.members
            name = choice(members)
            if (name.bot==False):
                break
    
    chosen = randint(0,maxpp-1)
    await ctx.send(f'{name} {pps[chosen]}')

@client.command()
async def pun(ctx):
    chosen = randint(0,maxp-1)
    chosenPun=puns[chosen]
    await ctx.send(chosenPun["pun"])
    await asyncio.sleep(5)
    await ctx.send(chosenPun["punchline"])


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def findvc(ctx, name):
    # find a guild by name
    guild = discord.utils.get(client.guilds, name="Social Center")
    # make sure to check if it's found
    if guild is not None:
        # find a channel by name
        channel = discord.utils.get(guild.voice_channels, name=name)
    await ctx.send(channel.id)

@client.command()
async def mem(ctx):
    channel1 = client.get_channel(758013927950123208)
    channel2 = client.get_channel(758014182032408608)
    members1 = channel1.members
    members2 = channel2.members
    print(channel1, channel2)
    print(members1, members2)

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

client.run('NzYwNTcyMTk1NjU4MjY4Njgy.X3OADg.XvgF1XvJqwHhg80hDbwle7gIGKs')

