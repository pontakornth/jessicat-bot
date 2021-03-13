import random
import math
import discord
from discord.ext import commands


class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sqrt(self, ctx: commands.Context, raw_n: str):
        try:
            converted_n = float(raw_n)
            await ctx.send(str(math.sqrt(converted_n)))
        except ValueError:
            await ctx.send("Invalid input. The input must be a number")

    @commands.command()
    async def mod(self, ctx: commands.Context, raw_numerator: str, raw_denominator: str):
        try:
            converted_numerator = int(raw_numerator)
            converted_denominator = int(raw_denominator)
            # pow takes third argument for modulo
            # This is more efficient that % operator for large number
            await ctx.send(str(pow(converted_numerator, 1, mod=converted_denominator)))
        except ValueError:
            await ctx.send("Invalid input. All inputs must be integers.")

    @commands.command()
    async def random(self, ctx: commands.Context, start: str, stop:str =""):
        try:
            start_num = int(start)
            if not stop:
                random_result = random.randrange(1, start_num)
                await ctx.send(f"Random result from 1 to {start_num} is {random_result}")
            else:
                stop_num = int(stop)
                random_result = random.randrange(start_num, stop_num)
                await ctx.send(f"Random result from {start_num} to {stop_num} is {random_result}")
        except ValueError:
            await ctx.send("The number is invalid.")