from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Your Full Name"
    username = os.getlogin()
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p>Name: {full_name}</p>
        <p>Username: {username}</p>
        <p>Server Time (IST): {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)