import discord
import random
from discord.ext import commands
import asyncio
import string

# Configuração do bot e intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Banco de dados de pontos
user_points = {}

# Respostas simuladas para o terminal
terminal_responses = {
    "ls": "📁 Documentos  Downloads  Imagens  Música  Vídeos\n🗂️ Nada para acessar aqui.",
    "cd": "🛑 Permissão negada para acessar essa pasta.",
    "mkdir": "🛠️ Pasta criada... Não! Ops, o administrador bloqueou.",
    "rm -rf /": "💥 Você tentou deletar tudo! Simulação salva sua vida.",
    "sudo": "😅 Você não é root, tente mais tarde.",
    "ping google.com": "📡 PING google.com: icmp_seq=1 ttl=117 time=20.3 ms",
    "whoami": "👤 Você é o mestre deste terminal!",
    "exit": "🖥️ Não é possível sair deste terminal. Está preso!",
}

# Função para gerar strings aleatórias
def gerar_string_aleatoria(tamanho):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

# Comando de terminal
@bot.tree.command(name="terminal", description="Simula comandos de terminal de forma interativa.")
async def terminal(interaction: discord.Interaction, comando: str):
    response = terminal_responses.get(
        comando, f"❌ Comando '{comando}' não reconhecido. Tente novamente."
    )
    await interaction.response.send_message(f"`{comando}`\n{response}")

# Comando de modo hacker
@bot.tree.command(name="hacker_mode", description="Simula um ambiente hacker (com humor).")
async def hacker_mode(interaction: discord.Interaction):
    messages = [
        "🕶️ Ativando o modo hacker...\n💻 Conexão perdida. Erro fatal.",
        "🚀 Tentando hackear a NASA... Não funcionou. Erro 404.",
        "🦠 Compilando vírus... Brincadeira! Apenas uma simulação.",
        "💳 Tentando acessar banco... Saldo: R$0,00.",
    ]
    await interaction.response.send_message(random.choice(messages))

# Comando para contar piadas
@bot.tree.command(name="piada", description="Conta uma piada para animar o servidor.")
async def piada(interaction: discord.Interaction):
    jokes = [
        "😂 Por que o livro de matemática ficou triste? Porque tinha muitos problemas.",
        "🐟 Qual é o peixe mais engraçado? O 'a-ha-ha-quinho'.",
        "💻 Por que o computador foi ao médico? Porque estava com um vírus.",
    ]
    await interaction.response.send_message(random.choice(jokes))

# Comando para exibir informações do perfil
@bot.tree.command(name="perfil", description="Exibe informações detalhadas de um usuário.")
async def perfil(interaction: discord.Interaction, usuario: discord.Member):
    embed = discord.Embed(title=f"Perfil de {usuario.name}", color=discord.Color.blue())
    embed.add_field(name="ID", value=usuario.id, inline=False)
    embed.add_field(
        name="Entrou no servidor",
        value=usuario.joined_at.strftime("%d/%m/%Y") if usuario.joined_at else "Data não disponível",
        inline=False,
    )
    embed.set_thumbnail(url=usuario.avatar.url)
    await interaction.response.send_message(embed=embed)

# Comando para criar enquetes
@bot.tree.command(name="enquete", description="Cria uma enquete interativa com duas opções.")
async def enquete(interaction: discord.Interaction, pergunta: str, opcao1: str, opcao2: str):
    mensagem = await interaction.response.send_message(f"📊 **{pergunta}**\n🔵 {opcao1}\n🟢 {opcao2}")
    await mensagem.add_reaction("🔵")
    await mensagem.add_reaction("🟢")

# Comando para gerenciar pontos
@bot.tree.command(name="pontos", description="Gerencia pontos de usuários (ver ou adicionar).")
async def pontos(interaction: discord.Interaction, usuario: discord.Member, adicionar: int = 0):
    if usuario.id not in user_points:
        user_points[usuario.id] = 0
    user_points[usuario.id] += adicionar
    await interaction.response.send_message(f"⭐ {usuario.name} agora tem {user_points[usuario.id]} pontos!")

# Comando /hackear (simula "hackear" um usuário)
@bot.tree.command(name="hackear", description=" Hackeia um usuário e envia informações.")
async def hackear(interaction: discord.Interaction, usuario: discord.Member):
    # Mensagem inicial no canal
    await interaction.response.send_message(f"💻 Iniciando hack em {usuario.mention}... Conectando aos servidores Debian...")

    # Mensagens simulando progresso
    mensagens_progresso = [
        "🔍 Conectando ao servidor Debian principal... Sucesso!",
        "🔐 Descriptografando credenciais do usuário...",
        f"🔓 Token de autenticação encontrado: {gerar_string_aleatoria(20)}",
        "📡 Extraindo IPs recentes conectados ao servidor...",
        f"🌐 IP detectado: 192.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}",
        "📂 Coletando logins recentes...",
        "🖥️ Mapas de dispositivos na rede encontrados.",
        "🔑 Chave SSH identificada. Exportando...",
    ]

    # Envia mensagens de progresso com atrasos
    for mensagem in mensagens_progresso:
        await asyncio.sleep(2)
        await interaction.followup.send(mensagem)

    # Dados fictícios finais
    senha_falsa = f"Token_{gerar_string_aleatoria(12)}"
    ip_falso = f"192.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    chave_ssh = f"ssh-rsa {gerar_string_aleatoria(64)} usuario@servidor"
    hash_senha = gerar_string_aleatoria(64)
    dispositivos_conectados = [
        f"Laptop - 192.168.1.{random.randint(1, 255)}",
        f"Smartphone - 192.168.1.{random.randint(1, 255)}",
        f"Servidor Local - 192.168.1.{random.randint(1, 255)}",
    ]
    logins_recentes = [
        f"Login em {ip_falso} às {random.randint(10, 23)}:{random.randint(10, 59)}",
        f"Login em 10.0.{random.randint(0, 255)}.{random.randint(0, 255)} às {random.randint(10, 23)}:{random.randint(10, 59)}",
    ]

    # Formata o resultado final
    embed = discord.Embed(title=f"💻 Informações Hackeadas de {usuario.name}", color=discord.Color.red())
    embed.add_field(name="🔑 Nome", value=usuario.name, inline=False)
    embed.add_field(
        name="📅 Data de Entrada no Servidor",
        value=usuario.joined_at.strftime("%d/%m/%Y") if usuario.joined_at else "Desconhecida",
        inline=False,
    )
    embed.add_field(name="🔒 Senha do Token", value=senha_falsa, inline=False)
    embed.add_field(name="🌐 IP Principal", value=ip_falso, inline=False)
    embed.add_field(name="🔐 Chave SSH", value=chave_ssh, inline=False)
    embed.add_field(name="🔓 Hash de Senha", value=hash_senha, inline=False)
    embed.add_field(name="📂 Logins Recentes", value="\n".join(logins_recentes), inline=False)
    embed.add_field(name="🖥️ Dispositivos na Rede", value="\n".join(dispositivos_conectados), inline=False)
    embed.set_footer(text="  Informações Coletadas Pelo Servidores Debian  !")

    # Envia o resultado final no chat
    await asyncio.sleep(2)
    await interaction.followup.send(embed=embed)

# Evento de inicialização
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"✅ Comandos sincronizados: {len(synced)} comandos")
    except Exception as e:
        print(f"❌ Erro ao sincronizar os comandos: {e}")
    print(f"🤖 {bot.user} está online e pronto para usar!")

# Insira o token do bot

bot.run(")