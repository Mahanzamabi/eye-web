from colorama import Fore
import sys
import socket
import os
import requests
import os
os.system('clear')
try:
    namesite = sys.argv[1]
    ipwebsite = socket.gethostbyname(namesite)
except:
    print(Fore.CYAN+'(Enter name site (command is run eye-web is python3 eye-web.py name site not https and http))')
    sys.exit()
import whois
run  = True
print('if get help typed help')
while run:
    print(Fore.GREEN,'')
    command = input('run command to site-->')
    command =command.lower()
    if command == 'help':
            os.system('clear')
            print(Fore.GREEN,'''
                help              (get help command)
                info             (get info site)
                open port        (ckeck open port site)
                get ip           (get ip website)
                send requests    (send requests ckeck online website)
                exit             (exit app)
    

            ''')
    elif command =='info':
        os.system('clear')
        print(whois.whois(namesite))
    elif command =='open port':
        os.system('clear')
        os.system(f'nmap {ipwebsite}')
    elif command =='get ip':
        os.system('clear')
        print(Fore.RED,f''' ip is:
        
        {ipwebsite}
        
        ''')
    elif command =='send requests':
        os.system('clear')
        print(requests.get('http://'+ipwebsite))
    elif command =='exit':
        os.system('clear')
        sys.exit()
    else:
        os.system('clear')
        print(Fore.YELLOW+'Unknown command')
        



    