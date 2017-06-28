
import requests, re, json, time, random
requests.packages.urllib3.disable_warnings()



# Added by Kenny McAvoy
# Last updated: June 28, 2017
from torrequest import TorRequest

def torIP():
	with TorRequest(proxy_port=9050, ctrl_port=9051, password='add your tor password')  as tr:
	  response = tr.get('http://ipecho.net/plain')
	  print(response.text)  # not your IP address






# Created by Alex Beals
# Last updated: June 28,2017 - Kenny McAvoy updated this from python 2 to 3 and added tor functionality

base_url = "https://polldaddy.com/poll/"
redirect = ""

useragents = []
current_useragent = ""

proxies = []
current_proxy = {"http":""}
current_proxy_num = -1


def get_all_useragents():
    f = open("useragent.txt", "r")
    for line in f:
        useragents.append(line.rstrip('\n').rstrip('\r'))
    f.close()

def choose_useragent():
    k = random.randint(0, len(useragents)-1)
    current_useragent = useragents[k]
    #print current_useragent

def get_all_proxies():
    f = open("proxy.txt", "r")
    for line in f:
        proxies.append(line.rstrip('\n').rstrip('\r'))
    f.close()

def choose_proxy():
    k = random.randint(0, len(proxies)-1)
    current_num = k
    current_proxy["http"] = proxies[k]


def vote_once(form, value):
    c = requests.Session()
    #Chooses useragent randomly
    choose_useragent()
    redirect = {"Referer": base_url + str(form) + "/", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "User-Agent": current_useragent, "Upgrade-Insecure-Requests":"1", "Accept-Encoding": "gzip, deflate, sdch", "Accept-Language": "en-US,en;q=0.8"}
    
    # Chooses proxy randomly
    choose_proxy()
    try:
        init = c.get(base_url + str(form) + "/", headers=redirect, verify=False, proxies=current_proxy)
    except:
        print("error with proxy")
        #proxies.remove(current_proxy_num)
        return None

    # Search for the data-vote JSON object
    data = re.search("data-vote=\"(.*?)\"",init.text).group(1).replace('&quot;','"')
    data = json.loads(data)
    # Search for the hidden form value
    pz = re.search("type='hidden' name='pz' value='(.*?)'",init.text).group(1)
    # Build the GET url to vote
    request = "https://polldaddy.com/vote.php?va=" + str(data['at']) + "&pt=0&r=0&p=" + str(form) + "&a=" + str(value) + "%2C&o=&t=" + str(data['t']) + "&token=" + str(data['n']) + "&pz=" + str(pz)
    try:
        send = c.get(request, headers=redirect, verify=False, proxies=current_proxy)
    except:
        print("error with proxy")
        #proxies.remove(current_proxy_num)
        return None
    
    return ("revoted" in send.url)

def vote(form, value, times, wait_min = None, wait_max = None):
    global redirect
    # For each voting attempt
    for i in range(1, times+1): 	
        b = vote_once(form, value)
        
        
        # If successful, print that out, else try waiting for 60 seconds (rate limiting)
        if not b:
            # Randomize timing if set
            if wait_min and wait_max:
                seconds = random.randint(wait_min, wait_max)
            else:
                seconds = 3
			
            
            print("Voted (time number " + str(i) + ")!")
            
            if i%5 == 0:
            	torIP()
            
        	
            time.sleep(seconds)
        
        else:
            print("Locked.  Sleeping for 60 seconds.")
            torIP()
            i-=1
            time.sleep(60)
            

# Initialize these to the specific form and how often you want to vote
poll_id = None
answer_id = None
number_of_votes = None
wait_min = None
wait_max = None

get_all_proxies()
get_all_useragents()
torIP()
vote(poll_id, answer_id, number_of_votes, wait_min, wait_max)


