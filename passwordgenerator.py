import os
import re
import secrets
import readline  # Required to stop escape sequences from displaying in input
from colorama import *
init(autoreset=True)

def clear(): os.system('cls||clear')  
def start():
    clear()
    print(f"""{Fore.LIGHTBLUE_EX}
                                                __                             __          
           ___  ___ ____ ____    _____  _______/ / ___ ____ ___  ___ _______ _/ /____  ____
          / _ \/ _ `(_-<(_-< |/|/ / _ \/ __/ _  / / _ `/ -_) _ \/ -_) __/ _ `/ __/ _ \/ __/
         / .__/\_,_/___/___/__,__/\___/_/  \_,_/  \_, /\__/_//_/\__/_/  \_,_/\__/\___/_/   
        /_/                                      /___/                                        
        \t\t\t\t\t\t{Fore.CYAN + Style.BRIGHT} Made by https://github.com/lucadado\n\n\n""")

    # Obtain a string of all printable characters
    printable = "".join(map(chr, range(33, 127)))
    
    
    ###################
    # User input      #
    ###################

    while True:
        try:
            length = int(input(f"{Fore.LIGHTBLUE_EX}Password Length: {Fore.RESET}"))
        except ValueError:
            print(f"{Fore.LIGHTRED_EX}Please provide a valid number! E.g. 1, 2, 3, 4..."); continue
        except KeyboardInterrupt: 
            print("")  # Fixes partial line issue with ZSH 
            exit(0)
        break

    while True:
        symbask = str(input(f"{Fore.LIGHTBLUE_EX}Do you want symbols? [Y, n]{Fore.RESET} ")).lower()
    
        if symbask in ("yes", "y", ""):        
            password = "".join(secrets.choice(printable) for _ in range(length))
            print(f"{Fore.LIGHTBLUE_EX}Password: {Fore.LIGHTYELLOW_EX}{password}")
            break
        elif symbask in ("no", "n"):
            password = "".join(secrets.choice(re.sub(r"[^\w]|_", "", printable)) for _ in range(length))
            print(f"{Fore.LIGHTBLUE_EX}Password: {Fore.LIGHTYELLOW_EX}{password}")
            break
        else:
            print(f"{Fore.LIGHTRED_EX}Please provide a valid answer! y(es) or n(o)")
            continue


    ###################
    # Rating          #
    ###################

    # RATING  -- Could be improved as grading a password souly on length is incomplete.
    tmp = {
        32:f"{Fore.LIGHTBLUE_EX}Password Strength: {Fore.MAGENTA}Area51",
        26:f"{Fore.LIGHTBLUE_EX}Password Strength: {Fore.LIGHTGREEN_EX}Very Strong",
        20:f"{Fore.LIGHTBLUE_EX}Password Strength: {Fore.LIGHTGREEN_EX}Strong",
        16:f"{Fore.LIGHTBLUE_EX}Password Strength: {Fore.GREEN}Good",
        10:f"{Fore.LIGHTBLUE_EX}Password Strength: {Fore.LIGHTGREEN_EX}Great",
        6 :f"{Fore.LIGHTBLUE_EX}Password Strength: {Fore.LIGHTRED_EX}Weak",
        0 :f"{Fore.LIGHTBLUE_EX}Password Strength: {Fore.RED}Very Weak"
    }
    next((print(tmp[key]) for key in tmp.keys() if len(password) >= key), None)

if __name__ == '__main__': start()
