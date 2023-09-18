tb = '\t'
nl = '\n'


def intro():
    with open('Intro.txt') as fl:
        ln = fl.readline()
        c = 0
        while ln:
            print(ln, end='')
            c += 1
            if c == 24:
                print()
                input('Press ENTER to Continue...')
                c = 0
            ln = fl.readline()
            

def wait(ms = '\nPress Enter to Continue...'):
    input(ms)

def line(ch = '-', n = 80):
    print(ch*n)

def inpany(msg = 'Enter an Integer Value: ', v = 0):
    if type(v) == int:
        v = int(input(msg))
    elif type(v) == float:
        v = float(input(msg))
    else:
        v = input(msg)
    return v
