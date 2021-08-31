# Amazing! Core functionality is working great.
# note : beautify notification

from bananopy import banano as ban
from time import sleep
from datetime import datetime
import track
from sys import argv
from os import system as exec



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
                exec(r'notify\target\debug\notify.exe "Recieved ' + str(pending_now - pending_then) +  'BAN" "account = ' + accounts[i] + '"')
                balances['balances'][accounts[i]]['pending'] = pending_now
        sleep(5)
