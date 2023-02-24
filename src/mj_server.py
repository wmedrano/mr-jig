import logging
from quart import Quart

logger = logging.getLogger(__name__)
app = Quart(__name__)


@app.route('/')
async def hello_world():
    return 'Hello, World!'


def run(port: int):
    logger.info(f"Starging Quart server on port {port}.")
    app.run(port=port, debug=False)
