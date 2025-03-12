import subprocess
import termcolor

subprocess.call(["netsh", "wlan", "show", "PROFILES"])
wifi_name = input("[+] Enter the Name of Wifi You want to get password from: ")
output = subprocess.getoutput(f'netsh wlan show profile name="{wifi_name}" key=clear')
if len(output) > 60:
    print(output)
    print(termcolor.colored(f"[+] Check the Key Section to get Password", "green"))
else:
    print(termcolor.colored(f"[-] Check the wifi name you entered", "red"))
