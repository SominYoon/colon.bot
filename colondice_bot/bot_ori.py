import os

import discord
from discord import app_commands as app_
from discord.ext import commands

from random import randint

TOKEN = None
APP_ID = None

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents, application_id=APP_ID)


# 함수------------

def dice(a: int = 1, s: int = 6, f: bool = False):
    rlist :list = []
    a = abs(a)
    if (not f):
        for i in range(a):
            rlist.append(randint(1, s))
    else:
        for i in range(a):
            rlist.append(randint(-1, 1))
    
    return {"sum":sum(rlist), "list":rlist}

# ------------
@bot.event
async def on_ready():
    print(f'[ {bot.user} : Online ]')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)


@bot.tree.command(name="r", description="성공수 굴림")
async def COLON_ROLL(interaction: discord.Interaction, amount:app_.Range[int,1,200], threshold:app_.Range[int,1,100]= 1, side:threshold:app_.Range[int,1,100]=6)
    
    roll = dice(a= amount, s= side) 
    r_str:str = ""
    sd:int = 0
    
    for i,n in enumerate(roll["list"]):
        if n<=threshold:
            roll["list"][i] = f'**__`[{n}]`__**'
            sd += 1
        else:
            roll["list"][i] = f'`[{n}]`'

    sd_str = f"**```ansi\n[2;40m[2;33m(  {str(sd)}  )[0m[2;40m[0m\n```**"
    r_str += ' '.join(str(i) for i in roll["list"])



    d_box=discord.Embed(title=f'[{amount}d:{threshold}]', color=0xa51d2d)
    d_box.add_field(name="SUCCESS", value=sd_str)
    d_box.add_field(name="DICE", value=r_str)

    await interaction.response.send_message(embed=d_box, ephemeral=False)


bot.run(TOKEN)
