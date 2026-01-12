# Discord Cat Bot 2.0
# Updated: January 11, 2025
# Developed by Kaitlyn Hornbuckle (https://www.linkedin.com/in/kaitlynhornbuckle/)
# Purpose: Filter profanity and send a warning to the Discord user
# if their speech is offensive.

#####################################################################################
# This script utilizes the following AI model:
#
# unitary/toxic-bert               ---> https://huggingface.co/unitary/toxic-bert
# Apache License & Additional Info ---> https://github.com/unitaryai/detoxify
#####################################################################################

import re
import discord
import requests
from transformers import pipeline
from discord.ext import commands

# Bot Token
b_token = 'xxxxxxxxxx' #--> replace with your Discord bot token from https://discord.com/developers
                       # Critical Security Note:
                       #    It is highly advisable to pass in your token from an encrypted file
                       #    to avoid exposing the bot token to malicious users. An addition to this
                       #    part of the code is incoming in 2026.

# Load a pre-trained model for toxic-bert
classifier = pipeline("text-classification", model="unitary/toxic-bert")

# Initialize client content from Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Initialize bot client
bot = commands.Bot(command_prefix='!', intents=intents)

#---------------------
# Checks new message
#---------------------
@client.event
async def on_message(message):

    # Reset boolean so that message still has a chance to get deleted if necessary
    delete = False

    # Check that author exists
    if message.author == client.user:
        return

    # Get message
    msg = message.content
    
    # Filter the message for profanity
    results = classifier(msg)
    
    for result in results:
        # AI Model checks severity
        if result['score'] > 0.3: # Scale: 1.0 = severe, 0.0 = best                                                                                                                                                                                                                  
            delete = True
            
            # Log flagged message
            log = open('flagged_log.txt', 'a')
            username = message.author.name
            log.write(f'{username} said: {msg}\n')
            log.close()

    # Delete the original message
    if delete == True:
        await message.delete()
        await message.channel.send(f"Meow! Sorry, that's not an appropriate message by cat standards. :3")

#------------------------
# Checks edited message
#------------------------
@client.event
async def on_message_edit(before, after):

    # Reset boolean so that message still has a chance to get deleted if necessary
    delete = False

    # Check that author exists
    if before.author == client.user or after.author == client.user:
        return

    # Get message
    msg = after.content
   
    # Filter the message for profanity
    results = classifier(msg)
    
    for result in results:
          # AI Model checks severity
          if result['score'] > 0.3: # Scale: 1.0 = severe, 0.0 = best                                                                                                                                                                                                                  
              delete = True
              
              # Log flagged message
              username = message.author.name
              log.write(f'{username} said: {message}\n')

    # Delete the original message
    if delete == True:
        await before.delete()
        await before.channel.send(f"Meow! Sorry, that's not an appropriate message by cat standards. :3")

# Run the bot with your token
client.run(b_token)
