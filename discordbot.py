import discord
from pprint import pprint
# 輸入自己Bot的TOKEN碼


client = discord.Client()

@client.event
async def on_ready():
    print('Login As：', client.user)
    game = discord.Game('lol')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "test" or message.content == "Test":
        await message.channel.send('Hi')

    if message.content.startswith('!'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("?")
      else:
        await message.channel.send(tmp[1])

# Bot起動
client.run(OTk4ODI5NTkyNTgyMzExOTQ2.G_RlH2.gl7Rc-K4oiObff4RbP1CEZp1M0mm2VUj5lbXEg)
