import os, platform, time, sys
os.system("pip install requests")
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
xoss('\n\x1b[1;37m[●] Checking Update........✔️✔️');time.sleep(0.5)
os.system("git pull")
def Update():
    exit('\033[1;31m[●] Commands On Update Please Wait For Update ❤ ')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            xoss("\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 🍼🙂")
            xoss('\x1b[1;94m[●] Join My Group First 🎈')
            os.system('xdg-open https://www.facebook.com/groups/2791954394284501/')
            from refat import welcome
            welcome()
        elif bit == '32bit':
            xoss("\n\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 🍼🙂")
            xoss('\x1b[1;94m[●] Follow My Github First 🎈')
            os.system('xdg-open https://github.com/shariar987')
            from refat import welcome
            welcome()
        else:
            exit('\033[1;31m[●] Connection & Network Error 🤕')
Run()
