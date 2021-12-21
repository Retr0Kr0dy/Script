import subprocess

def get_system_info():
    info  = subprocess.check_output(['systeminfo'])
    info_file_name = "SystemInfo.txt"
    with open(info_file_name, 'wb') as key_output:
        key_output.write(info)  
get_system_info()
