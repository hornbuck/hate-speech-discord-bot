# Discord Cat Bot 2.0 - Commands
# Updated: January 11, 2025
# Developed by Kaitlyn Hornbuckle (https://www.linkedin.com/in/kaitlynhornbuckle/)
# Purpose: Allow users to run commands to unlock the following fun features:
#          /cat = Generate a random cat photo
#          /dog = Generate a random dog photo
#          /catfact = Generate a random cat fact
#          /dogfact = Generate a random dog fact
#          /learnroblox = Learn something random from Roblox Studio (bot returns a tutorial link from Roblox's API)
 
import re
import random
import discord
import requests
from discord.ext import commands

# Bot Token
b_token = 'xxxxxxxxxx' #--> replace with your Discord bot token from https://discord.com/developers
                       # Critical Security Note:
                       #    DO NOT write the token in plain text. It is highly advisable to pass in your token 
                       #    from an encrypted file to avoid exposing the bot token to malicious users. 
                       #    An addition to this line to make it easier for developers to implement is incoming in 2026.

# Initialize client content from Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Initialize bot client
bot = commands.Bot(command_prefix='!', intents=intents)

# Cat Command: generate photos from TheCatAPI
@bot.tree.command(name='cat', description='Generate a random cat photo.')
async def slash_command(interaction:discord.Interaction):
    url = 'https://api.thecatapi.com/v1/images/search'                                                                                                                                                                                                                                
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data[0]['url']
        await interaction.response.send_message(f'Here\'s a random cat picture: {image_url}')   
    
    else:
        await interaction.response.send_message('Sorry, I couldn\'t fetch a cat picture at the moment.')

# Dog Command: generate photos from TheDogAPI
@bot.tree.command(name='dog', description='Generate a random dog photo.')
async def slash_command(interaction:discord.Interaction):
    url = 'https://api.thedogapi.com/v1/images/search'                                                                                                                                                                                                                                
    response = requests.get(url)
  
    if response.status_code == 200:
        data = response.json()
        image_url = data[0]['url']
        await interaction.response.send_message(f'Here\'s a random dog picture: {image_url}')   
      
    else:
        await interaction.response.send_message('Sorry, I couldn\'t fetch a dog picture at the moment.')

# Cat Fact Command: generate a random fact about cats
@bot.tree.command(name='catfact', description='A random fact about cats appears!')
async def slash_command(interaction:discord.Interaction):
    file = open('catfacts.txt', 'r')
    lines = file.readlines()
    await interaction.response.send_message(f'🐱 **Cat Fact:** {random.choice(lines).strip()}\nI\'m an old cat though, so make sure to fact check me. Facts sometimes change over time. :3\n')
    file.close()

# Dog Fact Command: generate a random fact about dogs
@bot.tree.command(name='dogfact', description='A random fact about dogs appears!')
async def slash_command(interaction:discord.Interaction):
    file = open('dogfacts.txt', 'r')
    lines = file.readlines()
    await interaction.response.send_message(f'🐕 **Dog Fact:** {random.choice(lines).strip()}\nI\'m an old cat though, so make sure to fact check me. Facts sometimes change over time. :3\n')
    file.close()

# Learn Roblox Command: generate a random tutorial from robloxtutorials.txt
@bot.tree.command(name='learnroblox', description='Learn something random about Roblox Studio.')
async def slash_command(interaction:discord.Interaction):
    file = open('robloxtutorials.txt', 'r')
    lines = file.readlines()
    await interaction.response.send_message(f'🔷 Here\'s a random Roblox tutorial: {random.choice(lines).strip()}')
    file.close()

@bot.event
async def on_ready():
    await bot.tree.sync()

# Run bot with token
bot.run(b_token)
