from . import mj_server
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    port = int(os.getenv('PORT', 21894))
    mj_server.run(port=port)


if __name__ == '__main__':
    main()
