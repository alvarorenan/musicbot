import discord
from discord.ext import commands

class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Comandos:
?help - Todos os comandos disponiveis
?clear quantidade - apagará as mensagens anteriores com a quantia especificada
Comandos de imagem:
----- EM BREVE -----
Comandos de música:
?play - encontra a música no youtube e a reproduz em seu canal atual
?queue - exibe a fila de música atual
?skip - pula a música atual que está sendo reproduzida
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
   
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

             
       

    @commands.command(name="help", help="Todos os comandos disponiveis")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)

    @commands.command(name="clear", help="Limpa uma quantidade de mensagens")
    async def clear(self, ctx, arg):
        #extract the amount to clear
        amount = 5
        try:
            amount = int(arg)
        except Exception: pass

        await ctx.channel.purge(limit=amount)