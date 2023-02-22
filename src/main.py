from . import mj_discord
from . import mj_server
import os
import threading
import dotenv
import logging

logger = logging.getLogger(__name__)


def main():
    dotenv.load_dotenv()

    discord_token = os.getenv('DISCORD_TOKEN')
    assert discord_token is not None
    discord_client_id = os.getenv('DISCORD_CLIENT_ID')
    assert discord_client_id is not None
    threading.Thread(target=lambda: mj_discord.run(
        discord_token=discord_token, discord_client_id=discord_client_id)).start()

    port = int(os.getenv('PORT', 21894))
    mj_server.run(port=port)


if __name__ == '__main__':
    main()
