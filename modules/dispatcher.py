from colorama import Fore, Style, init

import paramiko
import ftplib
import subprocess

init(autoreset=True)

isHttp = []


def dispatch_services(
    parsed_data, target, wordlist="wordlists/common.txt", savepath="gobuster.txt"
):
    for port in parsed_data["ports"]:
        service = port["service"]
        portNumber = port["port"]

        if service == "http" or service == "https":
            if len(isHttp) == 0:
                isHttp.append("An new http")
                print("HTTP detected")
                print("Running gobuster..")
                subprocess.run(
                    ["gobuster", "dir", "-u", target, "-w", wordlist, "-o", savepath],
                    text=True,
                )
                print(f"Gobuster ran successfully!.Saved file to:{Fore.BLUE}{savepath}")
            else:
                print("Already done directory enumeration")
                continue
        elif service == "ftp":
            print("ftp detected")
            server = ftplib.FTP()
            server.connect(target, portNumber)
            server.login("anonymous", "anonymous")
            print(f"{Fore.GREEN}Anonymous login allowed")

        elif service == "ssh":
            print("SSH detected")
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print("Trying default login..")
            ssh.connect(target, username='admin', password='password')

        else:
            print("No service found running on the server..")


if __name__ == "__main__":
    pass
