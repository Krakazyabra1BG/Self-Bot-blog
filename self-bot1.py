import discord
from discord.ext import commands
import os 
import asyncio


client = commands.Bot(command_prefix = '+', self_bot = True) #True - Команды юзать можете только вы!


token = input('Enter your token') #ввести токен в консоль

@bot.evenent
async def on_ready():
           print('New token has logged - (token)')

@client.command() #Команда ping, выдает пинг
async def ping(ctx):
  calc = bot.latency * 1000
  pong = round(calc)
  await ctx.message.delete()

  x = discord.Embed(title='**Pong**', description=f'{pong} `ms`', color=0xff0000) #red

  y = discord.Embed(title='**Pong**', description=f'{pong} `ms`', color=0xffff00) #yellow

  z = discord.Embed(title='**Pong**', description=f'{pong} `ms`', color=0x008000) #green

  if pong > 160: 
    msg = await ctx.send(embed=x)
    await msg.add_reaction('??')
  elif 80 <= pong <= 160:
    msg = await ctx.send(embed=y)
    await msg.add_reaction('??')
  elif pong < 80:
    msg = await ctx.send(embed=z)
    await msg.add_reaction('??')

@client.command 
@commands.has_permissions(manage_messages=True) #Команда say , в embed
    async def Say(self, ctx, *, message):
        await ctx.message.delete()

        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="Announcement!", icon_url=ctx.author.avatar_url)

        embed.add_field(name=f"Sent by {ctx.message.author}", value=str(message))

        embed.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

bot_access_ids = ['ID', 'ID'] #в место ID Вставьте ДС айди юзера. ИХ может быть сколько угодно вашей душе

@client.event
async def on_message(message):
    content = message.content[6:]
    if message.content.startswith('!find'):
        member = await message.guild.fetch_member(int(content))
        print(member)
    else:
        pass

@client.command()
async def find(ctx, id: int):
    member = await ctx.guild.fetch_member(id)
    print(member)

@client.command()
async def evaluate(ctx, *, cmd=None):
    try:
        eval(cmd)
        await ctx.send(f'Your bot friend executed your command --> {cmd}')
    except:
        print(f'{cmd} is an invalid command')
        await ctx.send(f'Your bot friend could not execute an invalid command --> {cmd}') 


client.run("(token)", bot = False) #Self-Bot start. в token Не вставлять ни чего!
