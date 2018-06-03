from flask import Flask

import settings
from api import *

app = Flask(__name__)
app.config.from_object(settings.Config)

init_api(app)


if __name__ == '__main__':
    app.run()
