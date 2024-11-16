# Amazing! Core functionality is working great, and the notifications look nice now.
# note : polish interface & file paths

from bananopy import banano as ban
from time import sleep
from datetime import datetime
import track
from sys import argv
from os import system as exec
from platform import system as getOS
from colorama import Fore, Style, init
init()

def is_negative(number):
    if ((0 + number) > 0):
        return False
    else:
        return True


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


if argv[1] == 'run':

    accounts = track.get_accounts()
    balances = ban.accounts_balances(accounts)

    while True:

        for i in range(len(accounts)):
            pending_now = ban.account_balance(accounts[i])['pending']
            pending_then = balances['balances'][accounts[i]]['pending']
            if ( pending_now != pending_then ):
                if ( not is_negative(pending_now - pending_then)):
                    print(f'Recieved {str(ban.ban_from_raw(str(pending_now - pending_then)))[0:4]}BAN at account {Fore.YELLOW}{accounts[i][0:7]}{Style.RESET_ALL}{accounts[i][7:61]}{Fore.GREEN}{accounts[i][60:65]}{Style.RESET_ALL}')
                    if (getOS() == 'Windows'):
                        exec(r'notify\target\debug\notify.exe ' + f'"Recieved {str(ban.ban_from_raw(str(pending_now - pending_then)))[0:4]}BAN" "at account {accounts[i]}"')
                    else:
                        exec(f'notify/target/debug/notify "Recieved {str(ban.ban_from_raw(str(pending_now - pending_then)))[0:4]}BAN" "at account {accounts[i]}"')
                balances['balances'][accounts[i]]['pending'] = pending_now
        sleep(5)
