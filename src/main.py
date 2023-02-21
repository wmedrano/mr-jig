from quart import Quart
import os


app = Quart(__name__)


@app.route('/')
async def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    port = int(os.getenv('PORT', '21894'))
    app.run(host='0.0.0.0', port=port)
