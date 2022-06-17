import discord
from discord.ext import commands
import asyncio
import youtube_dl
import os
import yt_dlp
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

default = "your user id here"
class Spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        scope = "user-library-read"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        self.user = self.sp.current_user()
        print(self.user["display_name"])
        print(self.user["followers"])

    # Get some simple stats given a spotify user
    @commands.command(name='spstat', description="generate some spotify stats")
    async def spstat(self, ctx, target: str = default):
        user = self.sp.user(target)
        res = self.sp.user_playlists(target)
        playlists = res['items']
        # Call next if next exists in the playlist dict to get all entries
        while res['next']:
            res = self.sp.next(res)
            playlists.extend(res['items'])
        playlist_count = len(playlists)
        await ctx.send(f"{user['display_name']} has {user['followers']['total']} followers and {playlist_count} "
                           f"playlist(s)")

def setup(bot):
    bot.add_cog(Spotify(bot))