import discord
import logging

logger = logging.getLogger(__name__)

discord_intents = discord.Intents.default()
discord_intents.message_content = True
discord_client = discord.Client(
    intents=discord_intents, command_prefix="!")
discord_command_tree = discord.app_commands.CommandTree(discord_client)


@discord_client.event
async def on_ready():
    logger.info(f"Syncing command tree.")
    await discord_command_tree.sync()


def run(discord_token: str, discord_client_id: str):
    logger.info(
        f"Discord client started. Invite at https://discord.com/api/oauth2/authorize?client_id={discord_client_id}&permissions=328565073920&scope=bot")
    discord_client.run(discord_token)
