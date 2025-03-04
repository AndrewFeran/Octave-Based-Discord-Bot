import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from oct2py import octave

# enable all intents
intents = discord.Intents.default()
intents.message_content = True  # required to read message content

# create bot instance and use cmd prefix for now
bot = commands.Bot(command_prefix="!", intents=intents)


# startup
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


# basic eval cmd
@bot.command()
async def eval(ctx, *, code: str):
    try:
        result = octave.eval(code)
        await ctx.send(result)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")



def main():
    # load .env
    load_dotenv()

    # access var
    bot_token = os.getenv("TOKEN")

    # start bot
    bot.run(bot_token)

if __name__ == "__main__":
    main()