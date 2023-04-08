import os
import traceback
from datetime import datetime
import discord
import asyncio
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

# The guild in which this slash command will be registered.
# It is recommended to have a test guild to separate from your "production" bot
TEST_GUILD = discord.Object(INSERT_GUILD_ID_HERE)


class ClaimView(discord.ui.View):
    @discord.ui.button(label='Use /Claim to Claim your Free NFTs', style=discord.ButtonStyle.primary)
    async def claim(self, interaction: discord.Interaction, button: discord.ui.Button, ):
        await interaction.response.send_message("Use slash commands /claim", ephemeral=True)


class MyClient(discord.Client):
    def __init__(self) -> None:
        # intents = discord.Intents.default()
        intents = discord.Intents.all()
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=TEST_GUILD)

    async def on_guild_join(self, guild: discord.Guild) -> None:
        embed = discord.Embed(title="Introducing the GAMERZ ULTIMATUM NFTs!",
                              description="**Introducing our latest collection of NFTs**\n__The 'GamerzUltimatum Collection'!__ \n\n***These digital Art are far more than just pretty pictures on your screen.***\n\nGet ready to feast your eyes on the most stunning collection of NFTs ever seen! Our latest drop features the most jaw-droppingly beautiful artwork you've ever laid eyes on - vibrant colors, intricate details, and stunning imagery that will transport you to another world. \n\nEach piece is a masterpiece in its own right. But that's not all, each NFT in this collection comes with a secret surprise hidden within the artwork lies a message or a clue that will lead you on a wild scavenger hunt through the crypto universe.",
                              colour=0xf6ff00,
                              timestamp=datetime.now())

        embed.set_author(name="BOT ULTIMATUM",
                         url="INSERT_BOT_AVATAR_URL_HERE",
                         icon_url="INSERT_BOT_AVATAR_URL_HERE

        embed.set_image(
            url="INSERT_IMAGE_URL_HERE")

        embed.set_thumbnail(
            url="INSERT_IMAGE_URL_HERE")

        embed.set_footer(text="Get Your Free NFT's straight to your wallets",
                         icon_url="https://cdn-icons-png.flaticon.com/128/5802/5802674.png")

        if guild.system_channel is not None:
            await guild.system_channel.send(content="@here\n\nHello, Hmm this is unexpected. NEW FEATURES FROM GU",
                                            embed=embed, view=ClaimView())
        else:
            print(f"Couldn't find a channel to send the message in guild {guild.name}")

        await self.tree.sync(guild=guild)

class ClaimNFTs(discord.ui.Modal, title='Claim Your NFTs'):
    wallet = discord.ui.TextInput(
        label='NFTs Wallet Address',
        style=discord.TextStyle.long,
        placeholder='Type Your Wallet Here...',
        required=False,
        max_length=1500,
    )

    async def on_submit(self, interaction: discord.Interaction):
        # self.wallet.value
        await interaction.response.send_message(f'NFT\'s ON DEEZ NUTS\nApril Fools (〜￣▽￣)〜', ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)


client = MyClient()


@client.tree.command(guild=TEST_GUILD, description="Claim NFTs")
async def claim(interaction: discord.Interaction):
    await interaction.response.send_modal(ClaimNFTs())


client.run(os.environ['TOKEN'])
