import subprocess
print("This line will be printed.")

#subprocess.call("echo \"* * * * * /bin/ping 10.34.1.1 -c 3\" | crontab -", shell=True) 
try:
    subprocess.check_output(shlex.split("echo \"* * * * * /bin/ping 10.34.1.1 -c 3\" | crontab -"))
except subprocess.CalledProcessError, e:
    looger.info("[ERROR]: cron update error")
    return 'false'