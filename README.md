# Cloudinary Upload Discord Bot
The code is a Discord bot written in Python that allows users to upload an image from a Discord channel to the Cloudinary cloud-based image and video management platform. 
<a href="https://replit.com/@zann5/cloudinaryupload-discordbot"><img src="https://repl.it/badge/github/username/repository" alt="Run on Repl.it"></a>

![Run on Replit.com](https://repl.it/badge/github/username/repository "Run on Replit.com")

## Features
- Responds to the command "/save" and takes the name of the Cloudinary tag as an argument.
- Built using the discord and requests Python libraries.
- Sets environment variables for the Discord bot token, the Cloudinary API key, and the API secret.
- Listens for messages starting with the "/save" command in a Discord channel.
- Retrieves the last image in the channel and uploads it to Cloudinary.
- Sends a confirmation message to the Discord channel to notify the user that the image has been uploaded.

## Secrets
Add these secrets to your replit at replit.com

Discord Bot Token from environment variable
- DISCORD_BOT_TOKEN = 

Cloudinary API information from environment variables
- CLOUD_NAME = 
- API_KEY = 
- API_SECRET =

## Fork on replit.com
- https://replit.com/@zann5/cloudinaryupload-discordbot