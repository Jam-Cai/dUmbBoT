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


# initiate bot
bot = commands.Bot(command_prefix="$")


# logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        ultraSlap = randint(0,20)
        if ultraSlap == 0:
            return '{0.author} smacked {1} to OBLIVION for 6969 damage!!! because *{2}*'.format(ctx, to_slap, argument)
        return '{0.author} smacked {1} for {3} damage because *{2}*'.format(ctx, to_slap, argument, randint(1,9999))

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.content.startswith("ello"):
        await message.author.send("Send help")

    # allow for commands 
    await bot.process_commands(message)

@bot.command(
    help="smacc your non-existant friends"
)
async def smacc(ctx, *, reason: Slapper):
    await ctx.send(reason)

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
    help = 'Leaderboard: +1 for winning RPS, -1 for losing' 
)
async def lb(ctx):
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
    output = "```css\n------ RPS GAME HiStOry :3 ------\n\n"
    for i in range(min(len(hist), 10)):
        output += hist[i] + '\n'
    output += "```"
    await ctx.send(output)


# run bot
bot.run('NzQ2NDc1ODYzOTQzNTQ0OTQy.X0A30g.d5arIsqSJf79RqWPRGFMjlqH04A')