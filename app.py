from flask import Flask
import os
import socket
from datetime import datetime
import sys

app = Flask(__name__)

@app.route("/")
def hello():

  html = "<h3>Hi {name}</h3>" \
         "<b>Hostname:</b> {hostname}<br/>" \
         "<b>Now:</b> {now}<br/>"  

  return html.format(name="world", hostname=socket.gethostname(), now= datetime.now())

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        raise Exception("You should provide port")

    params = sys.argv[1:]    
    port = params[0]
    print(port)
    app.run(host='0.0.0.0', port=port)
    