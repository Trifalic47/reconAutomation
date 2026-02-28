from colorama import Fore, Style, init
import subprocess

init(autoreset=True)

isHttp = []


def dispatch_services(
    parsed_data, target, wordlist="wordlists/common.txt", savepath="gobuster.txt"
):
    for port in parsed_data["ports"]:
        service = port["service"]

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

        elif service == "ssh":
            print("SSH detected")
