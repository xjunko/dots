""" install.py - idk man read the filename. """
__author__ = "xJunko"
__github__ = "xJunko"

import logging
import os


def main() -> int:
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.INFO)

    commands: list[str] = [
        "$ chmod +x -R ./config/",
        "$ chmod +x -R ./dots/",
        "+ Creating mkdir, just in case.",
        "$ mkdir -p ~/.config",
        "+ Installing config files",
        "$ cp -r ./config/* ~/.config",
        "+ Installing dotfiles",
        "$ cp -r ./dots/* ~",
        "+ LGTM, you're on your own with the packages.",
    ]

    for command in commands:
        if command.startswith("+"):
            logging.info(command[1:].strip())
        elif command.startswith("$"):
            os.system(command[1:])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
