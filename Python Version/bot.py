import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hey')

bot.run('OTI3OTMzNzYxNTUzODMzOTg0.YdRbqA.h5gU9LnVx16pM6PgwmPRB2Q-enU')