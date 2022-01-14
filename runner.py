import os
import sys
from pathlib import Path

from script.Scanner import Scanner


def checkPath(folder1: str, folder2: str) -> bool:
    if not os.path.exists(folder1):
        sys.exit(f'Path "{folder1}" does not exist')

    if not os.path.exists(folder2):
        sys.exit(f'Path "{folder2}" does not exist')

    if not os.path.isdir(folder1):
        sys.exit(f'Path "{folder1}" is not a folder')

    if not os.path.isdir(folder2):
        sys.exit(f'Path "{folder2}" is not a folder')

    return True


def main() -> None:
    folder1 = Scanner.ask("What is the path of the current version folder")
    folder2 = Scanner.ask("What is the path to the update folder")
    if checkPath(folder1, folder2):
        for path in Path(folder2).rglob("*"):
            if os.path.isfile(path):
                dest = str(path).replace(folder2, "")
                if os.path.isfile(f"{folder1}{dest}"):
                    print(f"{folder1}{dest}")


main()
