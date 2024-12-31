import discord
from discord.ext import commands
import os

# Intents are required to access specific features of Discord API
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# Bot prefix and instantiation
bot = commands.Bot(command_prefix="/", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

# Check if user has administrator permissions
def is_admin(ctx):
    return ctx.author.guild_permissions.administrator

# Command: Say (only admin users)
@bot.command()
@commands.check(is_admin)
async def say(ctx, *, message: str):
    await ctx.send(message)

# Command: Ping (for testing)
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Error handling for permission errors
@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command.")

# Run the bot (replace 'YOUR_BOT_TOKEN' with your actual bot token)
if __name__ == "__main__":
    bot.run(os.getenv("https://discord.com/api/webhooks/1323508811658428496/ZRC7GKO4wW24DQJo-TgergPJ26pyVQ4wpnx-CkeYCEuJDzVDWVESogT8P9TX-fNHwIPX"))
