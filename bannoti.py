
from sys import exit as die
from sys import argv
from colorama import Fore, Style, init
init()
import requests


def show_help() -> None:
    print("""
    bannoti.py <option>

    run : run the program
    --add : add an address to get notified for
    --remove : stop getting notifications for an address
    --gettracked : get tracked accounts
    --yesstartup : add program to startup (windows only)
    --nostartup : remove program from startup (windows only)
    
    Use Ctrl+C to exit.

    If this is your first time using Bannoti, I recommend you see the README (docs/README.md).""")

print(f"""{Fore.BLUE}

                     ____                          _   _
                     | __ )  __ _ _ __  _ __   ___ | |_(_)
                     |  _ \ / _` | '_ \| '_ \ / _ \| __| |
                     | |_) | (_| | | | | | | | (_) | |_| |
                     |____/ \__,_|_| |_|_| |_|\___/ \__|_|

                                        {Fore.YELLOW}Desktop notification tool for banano{Style.RESET_ALL} ({Fore.YELLOW}https://banano.cc{Style.RESET_ALL})
                                        {Fore.YELLOW} by @clocked07 {Style.RESET_ALL} ({Fore.YELLOW}https://github.com/clocked07{Style.RESET_ALL})


""")

try:
    argv[1]
except IndexError:
    show_help()
    die()

if argv[1] in ['--help', '-h', 'help'] or argv[1] not in ['--add', 'run', '--remove', '--gettracked', '--yesstartup', '--nostartup']:
    show_help()
    die()

from bananopy import banano as ban
from time import sleep
from datetime import datetime
from assets import track
from os import system as exec
from platform import system as getOS

print()

def is_negative(number):
    if ((0 + number) > 0):
        return False
    else:
        return True

def addToStartup(Name, Data) -> None:
    from os import system
    system(f'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "{Name}" /t REG_SZ /F /D "{Data}"')

def removeFromStartup(Name) -> None:
    from os import system
    system(f'REG DELETE "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "{Name}" /f')


if argv[1] == '--add':

    while True:
        try:
            track.add(input("Enter Address (^C to stop) : "))
        except KeyboardInterrupt:
            break

elif argv[1] == '--remove':

    present = track.get_accounts()

    for i in range(len(present)):
        print(f"[{i}] {present[i]}")

    track.remove(present[int(input('Remove : '))])

elif argv[1] == '--gettracked':
    print(track.get_accounts())

elif argv[1] == '--yesstartup':
    from os import getcwd
    addToStartup('Bannoti', f"{getcwd()}\\bannoti.exe run")

elif argv[1] == '--nostartup':
    removeFromStartup('Bannoti')


if argv[1] == 'run':

    accounts = track.get_accounts()
    balances = ban.accounts_balances(accounts)

    while True:

        try:

            for i in range(len(accounts)):

                pending_now = ban.account_balance(accounts[i])['pending']
                pending_then = balances['balances'][accounts[i]]['pending']

                if ( pending_now != pending_then ):

                    if ( not is_negative(pending_now - pending_then)):

                        print(f'Recieved {str(ban.ban_from_raw(str(pending_now - pending_then)))[0:4]}BAN at account {Fore.YELLOW}{accounts[i][0:7]}{Style.RESET_ALL}{accounts[i][7:61]}{Fore.GREEN}{accounts[i][60:65]}{Style.RESET_ALL}')

                        if (getOS() == 'Windows'):
                            exec(r'assets\notify.exe ' + f'"Recieved {str(ban.ban_from_raw(str(pending_now - pending_then)))[0:4]}BAN" "at account {accounts[i]}"')
                        else:
                            exec(f'assets/notify "Recieved {str(ban.ban_from_raw(str(pending_now - pending_then)))[0:4]}BAN" "at account {accounts[i]}"')

                    balances['balances'][accounts[i]]['pending'] = pending_now

            sleep(5)

        except requests.exceptions.ConnectionError:
            print(f"{Fore.RED}Internet connection lost.. {Style.RESET_ALL}", end="")
            while True:
                sleep(5)
                try:
                    requests.get('https://google.com')
                    break
                except:
                    pass
            print(f"{Fore.GREEN} Restored {Style.RESET_ALL}")
