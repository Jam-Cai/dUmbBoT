# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:13:19 2020

@author: Cai
"""

import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import logging
import random
from random import randint
from leaderboard import readLeaderboard, writeLeaderboard, playerLose, playerWin
from rpshistory import readHistory, writeHistory, addGame, tieGame
import time

# initiate bot
bot = commands.Bot(command_prefix=("baka ", "Baka ", "$"))
token = "dont even think about stealing my token"

# logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    channel = message.channel
    chance = randint(0,5)
    if message.content.startswith("james is "):
        await channel.send("no u")
    elif message.content.startswith("james cai is "):
        await channel.send("no u")
    
    if chance == 1:
        if message.content.startswith("im " or 'Im ' or 'IM '):
            await channel.send("Hi{}, i'm dumbbot".format(str(message.content)[2::]))
        
        elif message.content.startswith('i\'m ' or 'I\'m ' or 'I\'M '):
            await channel.send("Hi{}, i'm dumbbot".format(str(message.content)[3::]))
    # allow for commands 
    await bot.process_commands(message)

@bot.command()
async def marina(ctx):
    await ctx.send('https://soap2day.to/')


@bot.command()
async def TwoTruthOneLie(ctx):
    await ctx.send('WIP')

@bot.command()
async def jokes(ctx):
    question = ['Sometimes I tuck my knees into my chest and lean forward.',
    'Did you hear about the cheese factory that exploded inb France?',
    'Which bird has the worst manners?']
    answer = ['That’s just how I roll.','There was nothing left but de Brie.', 'A Mocking Bird']
    a = randint(0, len(question)-1)
    await ctx.send("**__{}__** \n   {} ".format(question[a], answer[a]))
@bot.command(
    help = 'Goes throught the whole process of baking bread'
)
async def bakebread(ctx):
    msg = ['MIxing the ingredients...','Kneading the dough...', 
    'Letting it rise...', 'Putting it in the oven...',
    'Done!', ':bread::bread::bread::bread::bread::bread::bread::bread::bread:']
    times = [ 2, 3, 5, 4, 0, 0]
    for i in range(0,len(msg)):
        await ctx.send(msg[i])
        time.sleep(times[i])

@bot.command(
    help= 'Chooses a random CPD episode'
)
async def choose_pd(ctx):
    episodes = {'1': 15, '2': 23, '3':23, '4':23, '5':22, '6':22, '7':20}
    season = randint(1,7)
    episode = randint(0, episodes[str(season)])
    await ctx.send('Chicago PD: Season {}, episode {}'.format(season, episode))

@bot.command(
    help= 'Chooses a random CMED episode'
)
async def choose_med(ctx): 
    episodes = {'1': 18, '2': 23, '3':20, '4':22, '5':20}
    season = randint(1,5)
    episode = randint(0, episodes[str(season)])
    await ctx.send('Chicago Med: Season {}, episode {}'.format(season, episode))

@bot.command(
    help= 'Chooses a random CFIRE episode'
)
async def choose_fire(ctx):
    episodes = {'1': 24, '2': 22, '3':23, '4':23, '5':22, '6':23, '7':22, '8':20}
    season = randint(1,8)
    episode = randint(0, episodes[str(season)])
    await ctx.send('Chicago Fire: Season {}, episode {}'.format(season, episode))

@bot.command(
    help='For the questions you can\'t google or calculate'
)
async def yesorno(ctx, *, arg):
    arg = arg.lower()
    theyesorno = ['Yes','no']
    
    if 'weeb' in arg and 'kevin' in arg and not 'not' in arg:
        await ctx.send('Yes, definitely')
    
    elif 'weeb' in arg and 'kevin' in arg and 'not' in arg:
        await ctx.send('No, definitely not')
    
    elif 'funny' in arg and 'marina' in arg and not 'not' in arg:
        await ctx.send('no')
    else:
        await ctx.send(random.choice(theyesorno))

@bot.command(
    help='I swear I\'m not a furry'
)
async def uwu(ctx,*, arg = None):
    if arg == None:
        channel = ctx.channel
        msg = await channel.history(limit=2).flatten()
        arg = msg[1].content
    # the length of the input text 
    length = len(arg) 
      
    # variable declaration for the output text 
    output_text = '' 
      
    # check the cases for every individual character 
    for i in range(length): 
          
        # initialize the variables 
        current_char = arg[i] 
        previous_char = '&# 092;&# 048;'
          
        # assign the value of previous_char 
        if i > 0: 
            previous_char = arg[i - 1] 
          
        # change 'L' and 'R' to 'W' 
        if current_char == 'L' or current_char == 'R': 
            output_text += 'W'
          
        # change 'l' and 'r' to 'w' 
        elif current_char == 'l' or current_char == 'r': 
            output_text += 'w'
          
        # if the current character is 'o' or 'O' 
        # also check the previous charatcer 
        elif current_char == 'O' or current_char == 'o': 
            if previous_char == 'N' or previous_char == 'n' or previous_char == 'M' or previous_char == 'm': 
                output_text += "yo"
            else: 
                output_text += current_char 
          
        # if no case match, write it as it is 
        else: 
            output_text += current_char 
  
    await ctx.send(output_text)

@bot.command(
    help= 'A random number from 1 to the number you specified'
)
async def rand_number(ctx, arg):
    await ctx.send(str(randint(1,int(arg))))

@bot.command(
    help= 'Do this if you want to lower your self-esteem'
)
async def roast(ctx):
    roasts = [
        'Grab a straw, because you suck','Brains aren’t everything. In your case they’re nothing',
    'You are proof that evolution can go in reverse','Stupidity’s not a crime, so you’re free to go',
    'You’re so fat you could sell shade',
    'It looks like your face caught fire and someone tried to put it out with a hammer',
    'I’m not a proctologist, but I know an asshole when I see one',
    'People clap when they see you. They clap their hands over their eyes',
    'I thought of you today. It reminded me to take out the trash',
    'You bring everyone so much joy, when you leave the room','I’m not a nerd, I’m just smarter than you',
    'Your face makes onions cry',' You’re the reason God created the middle finger',
    'Light travels faster than sound which is why you seemed bright until you spoke',
    'It’s impossible to underestimate you','You are so full of shit, the toilet’s jealous',
    'You just might be why the middle finger was invented in the first place',
    'You’re a grey sprinkle on a rainbow cupcake',
    'If your brain was dynamite, there wouldn’t be enough to blow your hat off',
    'You have so many gaps in your teeth it looks like your tongue is in jail',
    'Hold still. I’m trying to imagine you with personality']
    await ctx.send(random.choice(roasts))
@bot.command(
    help= 'Thumbs'
)
async def thumbs(ctx):
    await ctx.send(':+1::-1:')
@bot.command(
    help= "Sends a poop"
)
async def poop(ctx):
    await ctx.send(":poop:")

@bot.command()
async def anime(ctx):
    if str(ctx.author) == 'kjsnkla#5133' :
        await ctx.send("https://www.youtube.com/watch?v=oHg5SJYRHA0")
    else:
        await ctx.send("https://myanimelist.net/topanime.php")

@bot.command()
async def weebmeter(ctx):
    if str(ctx.author) == 'kjsnkla#5133':
        await ctx.send("You are 101% weeb")
    else:
        await ctx.send('You are {}% weeb'.format(randint(0,100)))    

@bot.command(
    help="Smacc your non-existant friends"
)
async def smacc(ctx):
    to_slap = random.choice(ctx.guild.members)
    slap = randint(0,10)

    onesmack = randint(0,20)
    if onesmack == 1:
        await ctx.send( '{0.author} harnessed the power of GOD and ANIME! Dealing an infinte amount of damage to  {1} !!'.format(ctx, to_slap))
    
    elif slap == 0:
        await ctx.send( '{0.author} smacked {1} to OBLIVION for 696969 damage!!!'.format(ctx, to_slap))
    elif slap == 1:
        await ctx.send( '{0.author} is so weak that they broke their fishbone arm! Dealing 1 damage to {1} and dealing 420 damage to themselves!!'.format(ctx, to_slap))
    else:
        await ctx.send('{0.author} smacked {1} for {2} damage'.format(ctx, to_slap, randint(1,9999)))

    
@bot.command(
help = "Play Rock Paper Scissors with a bot" 
)
async def bot_rps(ctx):
    msg = await ctx.send("React to me!")
    def check(reaction,user):
        return user == ctx.message.author

    rps_list = ['\U0001F1F5','\U0001F1F7', '\U0001F1F8']
    for emoji in rps_list:
        await msg.add_reaction(emoji)

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)    
    except asyncio.TimeoutError:
        await ctx.send('You took too long')
    
    bot_choice = random.choice(rps_list)
    
    if bot_choice == str(reaction):
        await ctx.send('Tie')
    
    elif str(reaction) == rps_list[1]:
        if bot_choice == rps_list[0]:
            await ctx.send('Bot wins')
        else:
            await ctx.send('You win')
    elif str(reaction) == rps_list[0]:
        if bot_choice == rps_list[2]:
            await ctx.send('Bot wins')
        else:
            await ctx.send('You win')
    elif str(reaction) == rps_list[2]:
        if bot_choice == rps_list[1]:
            await ctx.send('Bot Wins')
        else:
            await ctx.send('You win')   
    await ctx.send("You picked {}\nBot picked {}".format(str(reaction),bot_choice))

            
@bot.command(
    help="Play rock-paper-scissors with ur highly degenerate friend, just tag them in place of <user>"
    )
async def rps(ctx, user: discord.User):
    timeout = 120

    rps_list = {'r':'\U0001F1F7','p':'\U0001F1F5', 's':'\U0001F1F8'}
    await ctx.send("{} challenged {} to rock paper scissors".format(ctx.author.name, user.name))
    await ctx.send("{} needs to react to this message to confirm within {} seconds!".format(user.name, timeout))
    def check(reaction, opponent):
            return opponent == user

    try: 
       await bot.wait_for('reaction_add', timeout=timeout, check = check)   
    except asyncio.TimeoutError:
        await ctx.send("{} has not reacted in time".format(user.name))
        return
    
    async def get_reaction(player):
        msg = await player.send("Choose one reaction within {} seconds!".format(timeout)) 
        
        for emoji in rps_list.values():
            await msg.add_reaction(emoji)

        def check(reaction,user):
            return user == player

        reaction = None
        user = None
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=timeout, check = check)    
        except asyncio.TimeoutError:
            await player.send('You took too long')
        else:
            await user.send("Go back to the channel to check results")
        return reaction, user

    result1, result2 = await asyncio.gather(get_reaction(ctx.author), get_reaction(user))
    if not all(result1) or not all(result2):
        await ctx.send("One of you took too long to pick :poop:, start challenge again")
        return
    rps1 = str(result1[0])
    player1 = result1[1].name
   
    player2 = result2[1].name
    rps2 = str(result2[0])
    await ctx.send("{} picked {}\n{} picked {}".format(player1, rps1, player2, rps2))

    if rps1 == rps2:
        await ctx.send('Tie :facepalm:')
        tieGame(player1, player2)
        return

    
    elif rps1 == rps_list['p'] and rps2 == rps_list['r'] or \
         rps1 == rps_list['r'] and rps2 == rps_list['s'] or \
         rps1 == rps_list['s'] and rps2 == rps_list['p']:
        winner = player1
        loser= player2
        await ctx.send("Winner is {} :partying_face:".format(player1))
    else:
        winner = player2
        loser = player1
        await ctx.send("Winner is {} :partying_face:".format(player2))


    playerLose(loser)
    playerWin(winner)
    addGame(winner, loser)

@bot.command(
    help = 'Leaderboard: +2 for winning RPS, -1 for losing' 
)
async def board(ctx):
    lead = readLeaderboard()
    lead = {k: v for k, v in sorted(lead.items(), key=lambda x: x[1], reverse=True)}
    output = "```yaml\n------ RPS GAME LEaDerBoARD :3 ------\n\n{:<10} {:<10}\n".format('NAME', 'SCORE')
    for player, score in lead.items():
        output += "{:<10} {:<10}\n".format(player,str(score))
    output += "```"
    await ctx.send(output)
@bot.command(
    help = 'RPS game history'
)
async def h(ctx):
    hist = readHistory()
    hist = hist[::-1]
    output = "```yaml\n------ RPS GAME HiStOry :3 ------\n\n"
    for i in range(min(len(hist), 20)):
        output += hist[i] + '\n'
    output += "```"
    await ctx.send(output)

    
# run bot
bot.run(token)
