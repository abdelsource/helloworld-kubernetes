from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/><b>Host IP:</b> {ip} <br/>"
	return html.format(name=os.getenv("NAME", "world"), hostname=host_name, ip=host_ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)