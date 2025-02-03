import discord
from discord.ext import commands, tasks
import asyncio

# Coloque o token do seu bot aqui
TOKEN = "SEU_TOKEN_AQUI"

# Defina os intents do bot
intents = discord.Intents.default()
intents.message_content = True  # Permite que o bot leia o conteúdo das mensagens

# Define o bot
class MyBot(commands.Bot):  # Classe do bot que usa commands.Bot
    def __init__(self):
        super().__init__(command_prefix="c", intents=intents)
        self.synced = False

    async def on_ready(self):
        if not self.synced:
            await self.tree.sync()  # Sincroniza os comandos de barra com o servidor
            self.synced = True
        print(f"{self.user} está online e pronto para uso!")

# Instância do bot
bot = MyBot()

# Tarefa para repetir mensagem
@tasks.loop(seconds=1)  # Repete a cada 5 segundos
async def repetir_mensagem(channel: discord.TextChannel):
    user_id = 677705088822804506  # ID do usuário a ser mencionado
    await channel.send(f"<@{user_id}>   auuuauaua!")

# Comando para começar a repetição da mensagem
@bot.tree.command(name="repetir", description="Começa a repetição da mensagem em intervalos de tempo.")
async def start_repeating(interaction: discord.Interaction):
    await interaction.response.send_message("Iniciando repetição da mensagem...")
    repetir_mensagem.start(interaction.channel)

# Comando para parar a repetição da mensagem
@bot.tree.command(name="parar", description="Para a repetição da mensagem.")
async def stop_repeating(interaction: discord.Interaction):
    if repetir_mensagem.is_running():
        repetir_mensagem.stop()
        await interaction.response.send_message("Repetição da mensagem foi parada.")
    else:
        await interaction.response.send_message("Não há repetição em andamento.")

# Inicia o bot
bot.run(" ")