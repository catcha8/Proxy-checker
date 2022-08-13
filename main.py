import requests,threading


def check(proxies):
    try:
        proxy = {'http': f'http://{proxies}','https':f'http://{proxies}'}
        r = requests.get("https://discord.gg/catcha", proxies=proxy)
        if r.status_code == 200:
            f = open("Valid.txt", "a")
            f.write(f"{proxies}")      
    except:
        i = open("Invalid.txt", "a")
        i.write(f"{proxies}")  
        pass


for proxies in open("proxies.txt","r+"):
    print("Checking -->",proxies)
    threading.Thread(target=check,args=(proxies,)).start()
