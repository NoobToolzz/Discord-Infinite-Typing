import requests, os, time, yaml, random

from pystyle import Write, Colors, Colorate, Center

from data.plugins import invalid_characters, user_agents
os.system('cls' if os.name == 'nt' else 'clear')

with open('config.yml') as f:
    config = yaml.safe_load(f)

# Settings
token = config['token']
showuseragent = config['settings']['showuseragent']

banner = """
________  .______________
\______ \ |   \__    ___/
 |    |  \|   | |    |   
 |    `   \   | |    |   
/_______  /___| |____|   
        \/               
Discord Infinite Typing
Github: @NoobToolzz

"""
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))

channelId = Write.Input("Channel ID: ", Colors.purple_to_blue, interval=0.008)
interval = Write.Input("Request Interval: ", Colors.purple_to_blue, interval=0.008)
requestAmount = Write.Input("Request Amount: ", Colors.purple_to_blue, interval=0.008)

if any(char in invalid_characters for char in channelId or interval or requestAmount):
    Write.Print("Error: Channel IDs cannot contain letters or symbols.\n", Colors.red_to_yellow, interval=0)
    Write.Print("Press any key to continue . . .", Colors.rainbow, interval=0)
    os.system('pause >nul')
    exit()

if interval == "":
    interval = 0
if channelId == "":
    Write.Print("Error: Channel ID must be given.", Colors.red_to_yellow, interval=0)
    channelId = 0
if requestAmount == "0" or requestAmount == "":
    Write.Print("Error: Request amount cannot be 0 or none. Continuing with 5.\n", Colors.red_to_yellow, interval=0)
    requestAmount = 5

print()

def SendRequest():
    count = 0
    for i in range(int(requestAmount)):
        user_agent = random.choice(user_agents)
        headers = {
            'Authorization': token,
            'user-agent': user_agent,
        }

        try:
            r = requests.post(f"https://discord.com/api/v9/channels/{channelId}/typing", headers=headers)

            if r.status_code != 204:
                Write.Print(f"Failed to send request: {r.text}\n", Colors.red_to_yellow, interval=0)
            else:
                count += 1
                if showuseragent:
                    Write.Print(f"[{count}] Successfully sent request | Code: 204 | User-Agent: {user_agent}\n\n", Colors.green_to_white, interval=0)
                else:
                    Write.Print(f"[{count}] Successfully sent request | Code: 204\n", Colors.green_to_white, interval=0)
                time.sleep(int(interval))

        except KeyboardInterrupt:
            print()
            Write.Print("Stopped by you.\n", Colors.purple_to_blue, interval=0)
            break
    
    print()
    Write.Print(f"Successfully sent {count} requests to channel {channelId}.\n", Colors.purple_to_blue, interval=0)
    Write.Print(f"Press any key to continue . . .", Colors.rainbow, interval=0)
    os.system('pause >nul')
    exit()

SendRequest()