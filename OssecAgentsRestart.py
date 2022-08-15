#!/bin/python3
# Read about this script you can at https://github.com/PodvoyskiyV/OssecAgentsRestart

# import necessary modules
import os
from pyfiglet import figlet_format
from termcolor import colored

# create banner
banner = figlet_format('AgentsRestart')
print(colored(banner, 'green'))

# create, fill and open the file where we will save active agents
os.system("/var/ossec/bin/agent_control -lc >> /scripts/active_agents.txt")
active_agents = open("/scripts/active_agents.txt", 'r')

# loop for restart all active agents
i = 0
for active_agent in active_agents:
    if i < 2:
        pass
    else:
        active_agent = active_agent.split()
        try:
            ID = active_agent[1][:-1]
        except IndexError:
            break
        command = "/var/ossec/bin/agent_control -R " + ID
        os.system(command)
    i += 1

# close and remove the file with active agents
active_agents.close()
os.system("rm -f /scripts/active_agents.txt")
