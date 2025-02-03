import discord
from discord import app_commands
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  # Para gerenciar e criar categorias e canais

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sincroniza os comandos de barra com o servidor
        await self.tree.sync()

client = MyClient()

@client.event
async def on_ready():
    print(f"Bot {client.user.name} está online e pronto para criar e apagar canais.")

# Comando para criar canais e categorias
@client.tree.command(name="criar", description="Cria a estrutura de canais no servidor.")
@app_commands.checks.has_permissions(administrator=True)
async def criar_canais(interaction: discord.Interaction):
    guild = interaction.guild

    await interaction.response.send_message("Criando novas categorias e canais...")

    # Categoria Conferir Canais
    conferir_canais = await guild.create_category("📋 Conferir Canais")
    await guild.create_voice_channel("🎙 TPM", category=conferir_canais)

    # Categoria T.O.M
    tom_category = await guild.create_category("📜 T.O.M")
    await guild.create_text_channel("✒️ mandamentos", category=tom_category)
    await guild.create_text_channel("🪶 tom", category=tom_category)

    # Categoria CENTRAL DO OVO
    central_ovo = await guild.create_category("🥚 CEMTRAL DO OVO")
    await guild.create_text_channel("🌐 chat oval", category=central_ovo)
    await guild.create_text_channel("⚙️ comandos", category=central_ovo)

    # Categoria Salas da T.O.M
    salas_tom = await guild.create_category("🌀 Salas da T.O.M")
    await guild.create_voice_channel("💨 tropa Maliciosa", category=salas_tom)
    await guild.create_voice_channel("⚖️ Justiça dos ovos", category=salas_tom)
    await guild.create_voice_channel("🐥 Pintinho do carlinhos", category=salas_tom)

    await interaction.followup.send("Estrutura de canais criada com sucesso!")

# Comando para apagar todos os canais e categorias
@client.tree.command(name="apagar", description="Apaga todas as categorias e canais do servidor.")
@app_commands.checks.has_permissions(administrator=True)
async def apagar_canais(interaction: discord.Interaction):
    guild = interaction.guild

    await interaction.response.send_message("Apagando todas as categorias e canais...")

    # Deletar todos os canais e categorias
    for category in guild.categories:
        for channel in category.channels:
            try:
                await channel.delete()
            except Exception as e:
                print(f"Erro ao deletar canal {channel.name}: {e}")
        try:
            await category.delete()
        except Exception as e:
            print(f"Erro ao deletar categoria {category.name}: {e}")

    await interaction.followup.send("Categorias e canais apagados com sucesso!")

# Lida com falta de permissões
@criar_canais.error
@apagar_canais.error
async def comando_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingPermissions):
        await interaction.response.send_message("Você não tem permissão para usar este comando.", ephemeral=True)

# Rodar o bot com o token

client.run("")