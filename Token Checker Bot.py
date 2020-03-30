import discord.ext
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import requests
#Modules that you need!

client=commands.Bot(command_prefix='!')#Prefix(You can change it to whatever you want!)

@client.event
async def on_ready():
	print('Bot is ready to Check a few Tokens! ;)')
	print('---------------------------------------')
	print('Token Checker Bot by EC2★Darky#9770')
	print('-------------------------------------')

client.remove_command("help")
#removes the help command!

@client.command(aliases=["Check"])
async def check(ctx, *, arg):
	headers = {'Content-Type': 'application/json', 'authorization': arg}
	url = 'https://discordapp.com/api/v6/users/@me/library'
	re = requests.get(url, headers=headers)
	if re.status_code == 200:
		await ctx.send("Token is Valid!")
	else:
		await ctx.send("Token is Invalid!")
#How this Command works, type !check and write behind the !check the token, then the Bot will say you if the token is Valid or Invalid!(Only works with User tokens!)

client.run('BOT TOKEN')
#Delete the text BOT TOKEN and put the Bot token in there!
