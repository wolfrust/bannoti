from platform import system as getsys
from os import system as run

def mv(a, b):

    if getsys() == 'Windows':
        run(f'MOVE {a} {b}')
    elif getsys() == 'Linux':
        run(f'mv {a} {b}')
