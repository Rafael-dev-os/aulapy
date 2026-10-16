import discord
import os
import random
from botl import random_number
from botl import random_shakephere
from botl import ask_gemini
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('hi how are you doing'):
        await message.channel.send("Great! what about you?")
    elif message.content.startswith('im doing great'):
            await message.channel.send("Ok!")
    elif message.content.startswith('rules?'):
         await message.channel.send("no rules!")
    elif message.content.startswith('random number?'):
             await message.channel.send(random_number())
    elif message.content.startswith('shakespeare please'):
         await message.channel.send(random_shakephere())
    
    elif message.content.startswith('meme'):
        images = random.choice(os.listdir('images'))
        with open(f'images/{images}', 'rb') as f:
            #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
            picture = discord.File(f)
        # Podemos então enviar esse arquivo como um parâmetro
        await message.channel.send(file=picture)
    else:
        await message.channel.send(ask_gemini(message.content))

client.run("")
