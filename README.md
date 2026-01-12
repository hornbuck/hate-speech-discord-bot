# Hate Speech Discord Bot

<img width="173" height="72" alt="Cat Bot App" src="https://github.com/user-attachments/assets/bceddc1b-1771-4c54-ac78-84dc2ab04bf4" /> <img width="540" height="72" alt="Cat Bot Example" src="https://github.com/user-attachments/assets/113450ed-3e4e-4eff-934d-2002ba05fd0a" />

Are you looking to eradicate hate speech in your Discord server? After loading a pre-trained Bert model (https://huggingface.co/unitary/toxic-bert), this bot, called Cat Bot 2.0, is customized to delete inappropriate messages on Discord servers and warns users if they overstep. It also allows them to play with fun cat, dog, and Roblox game design features. This not only makes the bot a responsible moderator, but also fun to interact with!

## How does it work?

Users can run the following commands in chat:  

`/cat` = Generate a random cat photo

`/dog` = Generate a random dog photo

`/catfact` = Generate a random cat fact

`/dogfact` = Generate a random dog fact

`/learnroblox` = Learn a random game design technique for Roblox Studio (bot returns a tutorial link from Roblox's public documentation (https://create.roblox.com/docs/tutorials/)  

Currently, this bot is live in Pawsitive Comedy's Discord server. This is a new and upcoming YouTube channel centered in inspiring entertainment and ethical game design. Feel free to check it out here: https://www.youtube.com/@pawsitivecomedy

## How can I connect this bot to my Discord server?
If you are a developer looking to customize different and unique features for your own bot, you will want to note a few things before launching your adapted code.

### 1. Security Implications
Each time you create a Discord bot as a developer (https://discord.com/developers), you will obtain its one-time token. When setting the bot live on your Discord server, you will need line 21 in *catbot2.py* and line 18 in *catbot2-commands.py* to read the token. **NEVER copy and paste this token directly as plaintext. Currently, this bot is missing input sanitization, so please keep that in mind when setting up your development environment. It is recommended to have these files read the bot's token from an encrypted file or as a request to a secure API service.**

### 2. Set Discord Bot's Permissions
In the Discord Developer portal linked in the previous step, visit the bot's settings. Check that **Message Content Intent** is enabled. You may also need to enable text permissions including **Send Messages** and additional options, depending on permissions you wish to grant the bot. Make sure to save the **Permissions Integer** generated from the **Bot Permissions** box when linking the bot to your server.

### 3. Affordable Method for 24/7 Runtime
If you want your bot to run for 24 hours on your Discord server, an affordable method is to run *catbot2-main.py* as an **always-on task** using *PythonAnywhere*. If this is of interest to you and you want to support the ongoing development of this project at the same time, you can purchase an affordable plan through the team's affiliate link: https://www.pythonanywhere.com/?affiliate_id=01086a68

## Upcoming Updates
This project is currently ongoing! In 2026, the following updates will come next:  

  --> input sanitization based on penetration tests  
  --> safer method of linking the Discord chat bot's token using encryption  
  --> documentation for setting up your own customizable Discord bot  
  --> GoDot game design tips feature  
  
These updates are still in progress.
