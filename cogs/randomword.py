import discord
from discord.ext import commands
from random_word import RandomWords
from PyDictionary import PyDictionary
dictionary=PyDictionary()
r = RandomWords()
class Randomword(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "rw", description = "Generate a random word")
    async def rw(self, member):
        rword = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective")
        channel = member.guild.system_channel
        await channel.send("{0}".format(rword))
    @commands.command(name = "defw", description = "Define a word")
    async def defw(self, member, word : str):
        channel = member.guild.system_channel
        definitionMeaning = dictionary.meaning(word)
        try:
            for i in definitionMeaning:
                definition = (",\n".join(str(x) for x in definitionMeaning[i]))
                definition = definition.replace('(', '').replace(')', '')
                meaning = (i + " // " "{0}".format(definition))
                await channel.send(meaning)
        except:
            await channel.send("Could not find a meaning for the word")
def setup(bot):
    bot.add_cog(Randomword(bot))