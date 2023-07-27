""" sync.py - copy dotfiles and then sanitize it a little bit """

__author__ = "xJunko"
__github__ = "xJunko"

import logging
import shutil
from pathlib import Path

# Global
HOME = Path.home()
CONFIG = HOME / ".config"

# Local
DOTS_LOCAL = Path.cwd() / "dots"
CONFIG_LOCAL = Path.cwd() / "config"

# Options
DOTS_TO_COPY: list[str] = [".zshrc", "Pictures/Pape/apply_pape.sh"]
CONFIG_TO_COPY: list[str] = ["bspwm", "sxhkd", "dunst", "rofi", "polybar"]


# copy methods
def copy_dots_to_local() -> int:
    logging.info("Copying dotfiles.")

    for dot_name in DOTS_TO_COPY:
        if not (dot_file := HOME / dot_name).exists():
            # Dotfiles are not that important.
            logging.error(f"Dotfile {dot_name} didnt exist, not poggers, continuing.")
            continue

        target_file = DOTS_LOCAL / Path(dot_name)
        target_file.parent.mkdir(exist_ok=True, parents=True)

        shutil.copy(dot_file, target_file)

    return 0


def copy_config_to_local() -> int:
    logging.info("Copying `.config` files.")

    for folder_name in CONFIG_TO_COPY:
        if not (folder := CONFIG / folder_name).exists():
            logging.error(f"Folder {folder_name} not found, failed to sync!")
            return 1

        target_folder = CONFIG_LOCAL / folder_name

        logging.info(f"Found folder {folder_name}, copying.")

        shutil.copytree(folder, target_folder, dirs_exist_ok=True)

    return 0


def pre_init() -> None:
    # loggin setup
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.INFO)

    # folder setup
    for required_folder in [DOTS_LOCAL, CONFIG_LOCAL]:
        required_folder.mkdir(exist_ok=True, parents=True)


def main() -> int:
    pre_init()

    for task in [copy_dots_to_local, copy_config_to_local]:
        if ret_code := task():
            return ret_code

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
