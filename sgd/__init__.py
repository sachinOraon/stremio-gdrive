import os
import json
from flask import Flask
from sgd.gdrive import GoogleDrive

app = Flask(__name__)
token = json.loads(os.environ.get("TOKEN"))
gdrive = GoogleDrive(token)
context = ('server.crt', 'server.key')

from sgd import routes
app.run(debug=False, port=5000, host='0.0.0.0', ssl_context=context)
