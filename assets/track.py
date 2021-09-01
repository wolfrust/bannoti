
def add(address):

    open('assets/track.ini', 'a').write(f'{address}\n')

def get_accounts():

    tracked = []

    for line in open('assets/track.ini', 'r').readlines():
        tracked.append(line.replace('\n', ''))

    return tracked

def remove(address):

    from assets import sysf

    new = open('tmp.ini', 'w')

    for line in open('assets/track.ini', 'r').readlines():

        if (line.replace('\n', '') != address):
            new.write(line)

    new.close()
    sysf.mv('tmp.ini', 'assets/track.ini')
