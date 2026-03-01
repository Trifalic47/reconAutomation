from modules.services import Scan

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        help="Enter the ip/web address of target",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Enter the file name in which to store the output",
    )
    parser.add_argument(
        "-i",
        "--initial",
        type=int,
        help="Enter the initial port scanning range",
        default=1,
    )

    parser.add_argument(
        "-w",
        "--wordlist",
        type=str,
        help="Enter the wordlist path",
        default="wordlists/common.txt",
    )

    parser.add_argument(
        "-f",
        "--final",
        type=int,
        help="Enter the final port scanning range",
        default=1000,
    )
    args = parser.parse_args()

    target = args.target
    output = args.output
    initial = args.initial
    final = args.final
    wordlist = args.wordlist

    scan = Scan(target, wordlist, initial, final)
    if output:
        scan.baseScan(fileName=output)
    else:
        scan.baseScan()
