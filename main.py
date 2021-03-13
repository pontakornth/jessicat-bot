import discord
import random
import logging
import aiohttp
import os
from discord.ext import commands
from dotenv import load_dotenv

# Cogs
from cogs.math_cog import MathCog

load_dotenv()

logging.basicConfig(level=logging.INFO)

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
bot = commands.Bot(command_prefix="$")


@bot.command()
async def power(ctx: commands.Context):
    power_level = int(random.uniform(0, 90000))
    await ctx.send(f"{ctx.author} has power of {power_level}")


@bot.command()
async def dog(ctx: commands.Context):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as response:
            data = await response.json()
            if data["status"] == "success":
                embed = discord.Embed()
                embed.image(url=data["message"])
                await ctx.send(embed=embed)

# Add cogs
bot.add_cog(MathCog(bot))

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
