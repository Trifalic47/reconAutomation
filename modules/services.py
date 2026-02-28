from colorama import Fore, Style, init
from modules.parser import parser
from modules.dispatcher import dispatch_services

import subprocess
import os
import json

init(autoreset=True)


class Scan:
    def __init__(self, host, wordlist, initial=1, final=1000):
        self._host = host
        self._wordlist = wordlist
        self._initial = initial
        self._final = final
        self._directoryName = host.replace(".", "_")
        # subprocess.run(["mkdir", "-p", directoryName])
        try:
            if not os.path.exists(self._directoryName):
                os.makedirs(f"output/{self._directoryName}")
        except FileExistsError:
            pass
        self._xml_output = f"output/{self._directoryName}/{host}.xml"
        self._gobusterSave = f"output/{self._directoryName}/{host}.gobuster"

    def baseScan(self, fileName=None):
        try:
            if fileName is None:
                scan = subprocess.run(
                    [
                        "sudo",
                        "nmap",
                        "--vv",
                        "-p",
                        f"{self._initial}-{self._final}",
                        "-sS",
                        "-sV",
                        "-oX",
                        self._xml_output,
                        "-O",
                        self._host,
                    ],
                    text=True,
                )
            else:
                scan = subprocess.run(
                    [
                        "sudo",
                        "nmap",
                        "--vv",
                        "-p",
                        f"{self._initial}-{self._final}",
                        "-sS",
                        "-oX",
                        self._xml_output,
                        "-sV",
                        "-O",
                        "-oN",
                        f"output/{self._directoryName}/{fileName}",
                        self._host,
                    ],
                    text=True,
                )
            print(scan.stdout)

            data = parser(self._xml_output)
            try:
                with open(
                    f"output/{self._directoryName}/{self._host}.json", "a"
                ) as file:
                    file.write(str(data))
            except Exception as e:
                print(e)
            dispatch_services(
                data, self._host, wordlist=self._wordlist, savepath=self._gobusterSave
            )
        except Exception as e:
            print(e)
