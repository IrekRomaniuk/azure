import subprocess
print("This line will be printed.")
subprocess.call("echo \"* * * * * /bin/ping 10.34.1.1 -c 3\" | crontab -", shell=True)