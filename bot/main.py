import os
import discord
from discord.ext import commands

intents = discord.Intents.all()

komi = commands.Bot(command_prefix={'!!'},intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

@komi.event
async def on_ready():
    print('!!!')

@komi.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Panes")
    await discord.Member.add_roles(member, role)
    print(f'{member} se le dio el rol: {role}')


@komi.group(name='magic',pass_context = True,invoke_without_command=True)
@commands.has_role("Magic")
async def magicDef(ctx):
    print('!!...')

@magicDef.command(name='now')
async def now(ctx):
    await ctx.channel.send(f"{ctx.author.name} los convoca a <@&790022020925882399> inmediatamente!")

@magicDef.command(name='night')
async def noche(ctx): 
    await ctx.channel.send(f"Esta noche se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")
    
@magicDef.command(name='a12')
async def a12(ctx): 
    await ctx.channel.send(f"A las 12 se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

if __name__ == "__main__":
    komi.run(TOKEN)
