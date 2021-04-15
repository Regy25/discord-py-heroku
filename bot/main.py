import os
import discord
from discord.ext import commands
import requests
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
    
@magicDef.command(name='a0')
async def a0(ctx):
        await ctx.channel.send(f"A las 0 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a030')
async def a030(ctx):
        await ctx.channel.send(f"A las 0:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1')
async def a1(ctx):
        await ctx.channel.send(f"A las 1 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a130')
async def a130(ctx):
        await ctx.channel.send(f"A las 1:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a2')
async def a2(ctx):
        await ctx.channel.send(f"A las 2 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a230')
async def a230(ctx):
        await ctx.channel.send(f"A las 2:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a3')
async def a3(ctx):
        await ctx.channel.send(f"A las 3 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a330')
async def a330(ctx):
        await ctx.channel.send(f"A las 3:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a4')
async def a4(ctx):
        await ctx.channel.send(f"A las 4 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a430')
async def a430(ctx):
        await ctx.channel.send(f"A las 4:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a5')
async def a5(ctx):
        await ctx.channel.send(f"A las 5 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a530')
async def a530(ctx):
        await ctx.channel.send(f"A las 5:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a6')
async def a6(ctx):
        await ctx.channel.send(f"A las 6 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a630')
async def a630(ctx):
        await ctx.channel.send(f"A las 6:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a7')
async def a7(ctx):
        await ctx.channel.send(f"A las 7 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a730')
async def a730(ctx):
        await ctx.channel.send(f"A las 7:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a8')
async def a8(ctx):
        await ctx.channel.send(f"A las 8 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a830')
async def a830(ctx):
        await ctx.channel.send(f"A las 8:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a9')
async def a9(ctx):
        await ctx.channel.send(f"A las 9 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a930')
async def a930(ctx):
        await ctx.channel.send(f"A las 9:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a10')
async def a10(ctx):
        await ctx.channel.send(f"A las 10 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1030')
async def a1030(ctx):
        await ctx.channel.send(f"A las 10:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a11')
async def a11(ctx):
        await ctx.channel.send(f"A las 11 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1130')
async def a1130(ctx):
        await ctx.channel.send(f"A las 11:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a12')
async def a12(ctx):
        await ctx.channel.send(f"A las 12 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1230')
async def a1230(ctx):
        await ctx.channel.send(f"A las 12:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a13')
async def a13(ctx):
        await ctx.channel.send(f"A las 13 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1330')
async def a1330(ctx):
        await ctx.channel.send(f"A las 13:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a14')
async def a14(ctx):
        await ctx.channel.send(f"A las 14 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1430')
async def a1430(ctx):
        await ctx.channel.send(f"A las 14:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a15')
async def a15(ctx):
        await ctx.channel.send(f"A las 15 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1530')
async def a1530(ctx):
        await ctx.channel.send(f"A las 15:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a16')
async def a16(ctx):
        await ctx.channel.send(f"A las 16 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1630')
async def a1630(ctx):
        await ctx.channel.send(f"A las 16:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a17')
async def a17(ctx):
        await ctx.channel.send(f"A las 17 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1730')
async def a1730(ctx):
        await ctx.channel.send(f"A las 17:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a18')
async def a18(ctx):
        await ctx.channel.send(f"A las 18 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1830')
async def a1830(ctx):
        await ctx.channel.send(f"A las 18:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a19')
async def a19(ctx):
        await ctx.channel.send(f"A las 19 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a1930')
async def a1930(ctx):
        await ctx.channel.send(f"A las 19:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a20')
async def a20(ctx):
        await ctx.channel.send(f"A las 20 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a2030')
async def a2030(ctx):
        await ctx.channel.send(f"A las 20:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a21')
async def a21(ctx):
        await ctx.channel.send(f"A las 21 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a2130')
async def a2130(ctx):
        await ctx.channel.send(f"A las 21:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a22')
async def a22(ctx):
        await ctx.channel.send(f"A las 22 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a2230')
async def a2230(ctx):
        await ctx.channel.send(f"A las 22:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a23')
async def a23(ctx):
        await ctx.channel.send(f"A las 23 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a2330')
async def a2330(ctx):
        await ctx.channel.send(f"A las 23:30 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@magicDef.command(name='a24')
async def a24(ctx):
        await ctx.channel.send(f"A las 24 horas se juega <@&790022020925882399>, preparen sus mazos. Respondan con <:mtg:793655716862754847> para confirmar")

@komi.command(name='commander')
async def commander(ctx):
        params = {'format': 'json', 'q': '(t:legend t:creature) or (o:"can be your commander")'}
        for i in range(3):
            req1 = requests.get("https://api.scryfall.com/cards/random", 
                                params=params)
            req1_data = req1.json()
            await ctx.send(req1_data['image_uris']['normal'])
        
if __name__ == "__main__":
    komi.run(TOKEN)
