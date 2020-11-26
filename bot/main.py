import os
import discord
from discord.ext import commands
#test
intents = discord.Intents.all()

komi = commands.Bot(command_prefix={'!k','!k '},intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

@komi.event
async def on_ready():
    print('!!!')

@komi.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Bot Tester")
    await discord.Member.add_roles(member, role)
    print(f'{member} se le dio el rol: {role}')

@komi.command()
async def ping(ctx):
    await ctx.channel.send("pong")
    
if __name__ == "__main__":
    komi.run(TOKEN)