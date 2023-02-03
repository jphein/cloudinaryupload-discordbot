import discord
import requests
import os
from io import BytesIO
import cloudinary

##The code is a Discord bot written in Python that allows users to upload an image from a Discord channel to the Cloudinary cloud-based image and video management platform. The bot responds to a command "/save" and takes the name of the Cloudinary tag as an argument.

##The bot is built using the discord and requests Python libraries. The discord library is used to interact with the Discord API to receive and send messages, while the requests library is used to download an image from a URL.

##The bot starts by setting environment variables for the Discord bot token, the Cloudinary API key, and the API secret. These environment variables are retrieved using os.environ.

##The bot listens for messages starting with the "/save" command in a Discord channel. If a message starts with this command, the bot retrieves the last image in the channel and downloads it using requests.get(last_image_url). The downloaded image is then uploaded to Cloudinary using the cloudinary.uploader.upload function. The name of the tag is passed as an argument to the tags parameter in the cloudinary.uploader.upload function.

##Finally, the bot sends a confirmation message to the Discord channel to notify the user that the image has been uploaded to Cloudinary with the specified tag.

##The on_ready event handler is used to log a message in the console when the bot is ready and to print the invite URL to add the bot to a Discord server.

#Add these secrets to your replit at replit.com
# Discord Bot Token from environment variable
DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
# Cloudinary API information from environment variables
CLOUD_NAME = os.environ["CLOUD_NAME"]
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
#---------------------------------------------

# Initialize cloudinary
cloudinary.config(
  cloud_name = CLOUD_NAME,
  api_key = API_KEY,
  api_secret = API_SECRET
)

# Set intents for Discord Client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Event handler for when a message is sent on the discord server
@client.event
async def on_message(message):
    last_image_url = None

    # Check if the message starts with "/save" command
    if message.content.startswith("/save"):
        # Split the message to get the tags
        split_message = message.content.split(" ")
        if len(split_message) < 2:
            await message.channel.send("❌ Invalid command format. Usage: `/save tag1 tag2 ...`")
            return
        tags = split_message[1:]

        # Get the last image in the channel
        async for last_message in message.channel.history(limit=2):
            for attachment in last_message.attachments:
                if attachment.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    last_image_url = attachment.url
                    break
        if last_image_url is None:
            await message.channel.send("❌ Sorry, no image was found to save.")
            return

        # Download the image
        response = requests.get(last_image_url)
        image = BytesIO(response.content)

        # Upload the image to Cloudinary and add the tags
        response = cloudinary.uploader.upload(image, tags=tags)
        public_id = response['public_id']
        await message.channel.send(f"✅ Image uploaded to Cloudinary with ID: `{public_id}` and tags: `{', '.join(tags)}` 📷")

# Event handler for when the discord bot is ready
@client.event
async def on_ready():
    print("Bot is ready!")
    user = client.user
    invite_url = discord.utils.oauth_url(user.id, permissions=discord.Permissions.all())
    print("Invite URL:", invite_url)

# Start the Discord Bot
client.run(DISCORD_BOT_TOKEN)