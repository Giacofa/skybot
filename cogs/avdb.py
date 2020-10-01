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
        if not acft == None:
            found = False
            with open('lib/avdata.json', 'r') as f:
                data = json.load(f)
                f.close()
            for a in data:
                if a['designator'] == acft:
                    found = True
                    acftdata = a
            
            if found == True:
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_author(name=f'Data for: {acft}')
                embed.set_image(url=acftdata['img_url'])
                await ctx.send(embed=embed)
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_author(name=f'Basic Data')
                embed.add_field(name="**-----------**", value=f'''**ICAO:** {acftdata['designator']}
**Name and constructor:** {acftdata['name']}
**Type:** {acftdata['type']}
**WTC:** {acftdata['wtc']}
**APC:** {acftdata['apc']}''', inline=False)
                await ctx.send(embed=embed)
                embed = discord.Embed(color=discord.Color.blue())
                embed.set_author(name=f'Cruise Data')
                embed.add_field(name="**-----------**", value=f'''**Ceiling:** {acftdata['cruise']['ceiling']}
**Rate of climb:** {acftdata['cruise']['ROC']}
**TAS:** {acftdata['cruise']['TAS']}
**Mach:** {acftdata['cruise']['mach']}''', inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f'Aircraft "{acft}" not found.')

    
    @commands.command(name="loadacft")
    async def loadacft_command(self, ctx):
        if ctx.author.id == self.ownerid:
            # conn = mysql.connector.connect(
            #     host=str(self.db_host),
            #     user=str(self.db_username),
            #     password=str(self.db_password),
            #     database=str(self.db_name),
            # )
            # c = conn.cursor()
            pass
            

def setup(client):
    client.add_cog(avdbCommands(client))