import discord
import requests
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from io import BytesIO

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
CLOUD_NAME = os.environ["CLOUD_NAME"]
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]

cloudinary.config(
  cloud_name = CLOUD_NAME,
  api_key = API_KEY,
  api_secret = API_SECRET
)

# Discord bot token
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    last_image_url = None
    if message.content.startswith("/save"):
        # Get the tag
        split_message = message.content.split(" ")
        if len(split_message) != 2:
            await message.channel.send("❌ Invalid command format. Usage: `/save tag`")
            return
        tag = split_message[1]

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

        # Upload the image to Cloudinary
        try:
            result = cloudinary.uploader.upload(image, tags=[tag])
            await message.channel.send("✅ Image uploaded to Cloudinary with the `" + tag + "` tag successfully! 📷")
        except:
            await message.channel.send("❌ An error occurred while uploading the image.")

@client.event
async def on_ready():
    print("Bot is ready!")
    user = client.user
    invite_url = discord.utils.oauth_url(user.id, permissions=discord.Permissions.all())
    print("Invite URL:", invite_url)

client.run(os.environ.get("DISCORD_BOT_TOKEN"))