import discord
from discord.ext import commands
import asyncio
import datetime
import bs4
import random
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
class Misc(commands.Cog):
    """ Some extra commands"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def userid(self, ctx):
        newString = ctx.message.author.id
        print(ctx.author.mention)
        await ctx.send(" ".format(newString) + f"name{ctx.author.mention}")
    @commands.command(name = "news", description = "Generate some news")
    async def news(self, ctx, msg: int = 0):
        """ Pull some news from google """
        news_url = "https://news.google.com/news/rss"
        newsClient = urlopen(news_url)
        xml_page = newsClient.read()
        newsClient.close()
        soup_page = soup(xml_page, "html.parser")
        news_list = soup_page.findAll("item")
        counter = 0
        text = ""
        for news in news_list:
            if -1 + (msg * 3) < counter < 3 + (msg * 3):
                text += (news.title.text + "\n" + news.pubdate.text + "\n" + "-" * 60 + "\n")
                counter += 1
            else:
                counter += 1
        await ctx.send("Here are the top stories for today \n{0}".format(text))

    @commands.command(name = "ping", description = "Ping a member")
    async def ping(self, ctx, target: str, *, message_content: str = ""):
        """ Ping pong. Ping a member of your choice and send them a message"""
        guild = ctx.message.author.guild
        for member2 in guild.members:
            if target in str(member2).lower():
                print("{0}".format(member2))
                targetUser = str(member2).split("#")
                print(targetUser)
                user = discord.utils.get(guild.members, name=targetUser[0], discriminator=targetUser[1])
                text = str(user.id)
                await ctx.send("<@{0}> {1}".format(text, message_content))

    @commands.command(name = "roulette", description = "Generate a winning member in your guild/server")
    async def roulette(self, ctx):
        members2 = []
        for member in ctx.message.author.guild.members:
            members2.append(member)
        winner = members2[random.randint(0, len(members2) - 1)]
        await ctx.send("{0} wins!".format(winner))

    @commands.command(name = "warn", description = "Warn a member in your guild/server")
    async def warn(self, ctx, target: str, *, message=""):
        guild = ctx.message.author.guild
        foundMember = False
        for member2 in guild.members:
            if target in str(member2).lower() and foundMember == False:
                await member2.send("you have been warned for {0}".format(message))
                await ctx.send("Warned {0}".format(str(member2)))
                foundMember = True


def setup(bot):
    bot.add_cog(Misc(bot))


