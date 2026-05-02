import os
import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text
from ms4 import InfoTik  


gg = 0
bb = 0
console = Console()

# Join Telegram group (Ensure this URL is correct)
os.system('xdg-open https://t.me/n_n_5s ')
os.system('xdg-open https://www.instagram.com/n.n.5s ')

# Input target username
os.system('clear') 
print("""_______________________________________________
Wellcome to Our Tools🔥
\033[1;32mThis Tools Developer By AlnsaarAlyemeny
__________________________________________________
< > < > > 🇾🇪 TIKTOK-REPORT_Alnsaar 🇾🇪 < < > < > 
||||||||     √ https://t.me/n_n_5s  ||||||||
||||||||     √ https://t.me/N_S_R80 ||||||||
|||||||| √ www.instagram.com/n.n.5s ||||||||
||||||||              💀💀          ||||||||
================================================
\033[1;33mDEVELOPER ▶ AlnsaarAlyemeny
TEAM ▶︎AlnsaarAlyemeny
CEO   ▶︎@N_S_R80
CHANNEL  ▶︎https://t.me/NSR882
TOOLS NAME  ▶TIKTOK-REPORT_Alnsaar
================================================""")
user = input("\n\n\n[</>] Enter The Target Username : ")
info = InfoTik.TikTok_Info(user)

# Retrieve user info with error handling
try:
    nm = info.get('name', "")
    folo = str(info.get('followers', ""))
    following = str(info.get('following', ""))
    country = f"{info.get('country', '')} {info.get('flag', '')}"
    bio = info.get('bio', "")
    user_id = str(info.get('id', ""))
    private = str(info.get('private', ""))
    date = str(info.get('Date', ""))
    likes = str(info.get('like', ""))
except KeyError as e:
    console.print(f"Missing expected field: {e}", style="bold red")

def killman():
    # Example implementation; adjust as needed
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

def base_params():
    # Example implementation; adjust as needed
    return {
        "param1": "value1",
        "param2": "value2"
    }

def Report():
    global gg, bb
    url = "https://sf16-website-login.neutral.ttwstatic.com/obj/tiktok_web_login_static/falcon/tiktok/search-web-inapp/resource/css/5848.0026db87.css"
    headers = killman()
    params = base_params()
    try:
        res = requests.get(url, params=params, headers=headers)
        if '"status_code":13,"status_message":""' in res.text:
            os.system('clear')
            gg += 1
        else:
            os.system('clear')
            bb += 1
    except requests.RequestException as e:
        console.print(f"Request error: {e}", style="bold red")

def display_report():
    total = gg + bb
    
    table = Table(title="TIKTOK-REPORT_Alnsaar")
    table.add_column("Type", justify="center", style="cyan", no_wrap=True)
    table.add_column("Count", justify="center", style="magenta")
    
    table.add_row("Good Report", Text(str(gg), style="green"))
    table.add_row("Bad Report", Text(str(bb), style="red"))
    table.add_row("Total", Text(str(total), style="yellow"))
    table.add_row("Dev", "AlnsaarAlyemeny")
    table.add_row("User", Text(user, style="cyan"))
    table.add_row("Name", Text(nm, style="cyan"))
    table.add_row("Followers", Text(folo, style="green"))
    table.add_row("Following", Text(following, style="yellow"))
    table.add_row("Country", Text(country, style="blue"))
    table.add_row("Bio", Text(bio, style="magenta"))
    table.add_row("ID", Text(user_id, style="cyan"))
    table.add_row("Private", Text(private, style="red" if private == "True" else "green"))
    table.add_row("Date", Text(date, style="magenta"))
    table.add_row("Likes", Text(likes, style="green"))
    console.print(table)

# Main loop
while True:
    try:
        Report()
        display_report()
    except Exception as e:
        console.print(f"Error reporting: {e}", style="bold red")
