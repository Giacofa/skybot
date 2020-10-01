import discord
from discord.ext import commands

import os, json
from dotenv import load_dotenv
load_dotenv()

class avdbCommands(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.ownerid = int(os.getenv('OWNER_ID'))

        self.db_host = os.getenv('db_host')
        self.db_username = os.getenv('db_username')
        self.db_password = os.getenv('db_password')
        self.db_name = os.getenv('db_database_name')
    
    @commands.command(name="acft", aliases=['Acft', 'ACFT'])
    async def acft_command(self, ctx, acft = None):
        print(acft)
    
    @commands.command(name="loadacft")
    async def loadacft_command(self, ctx):
        if ctx.author.id == self.ownerid:
            await ctx.send('Hello!')
        else:
            await ctx.send('No')

def setup(client):
    client.add_cog(avdbCommands(client))