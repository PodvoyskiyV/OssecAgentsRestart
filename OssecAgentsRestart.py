import os
import subprocess
from pyfiglet import figlet_format
from termcolor import colored

banner = figlet_format('AgentsRestart')
print(colored(banner, 'green'))

os.system("echo Hello from the other side!")

new = subprocess.run(["echo", "Hello from the other side!"])
print(new)

os.system("ls")
os.system("cd .. | ls")

home_dir = subprocess.run(["cd", ".."])
print(home_dir)


list_files = subprocess.run(["/var/ossec/bin/agent_control", "-lc"])
print(list_files)

list_files = subprocess.run(["ls", "/"])
print(list_files)
