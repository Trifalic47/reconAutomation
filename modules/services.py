import subprocess
from colorama import Fore, Style, init
import os

init(autoreset=True)


class Scan:
    def __init__(self, host, initial=1, final=1000):
        self._host = host
        self._initial = initial
        self._final = final
        self._directoryName = host.replace(".", "_")
        # subprocess.run(["mkdir", "-p", directoryName])
        if not os.path.exists(self._directoryName):
            os.makedirs(f"output/{self._directoryName}")
        self._xml_output = f"output/{self._directoryName}/{host}.xml"

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
                    capture_output=True,
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
                    capture_output=True,
                    text=True,
                )
            print(scan.stdout)
        except Exception as e:
            print(e)
