from django.http import HttpResponse
import os
import time
import subprocess

def htop(request):
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
    return HttpResponse(response)