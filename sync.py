import shutil
from pathlib import Path

# Home
HOME: Path = Path("/home/junko/")
CONFIG: Path = HOME / ".config"
REPO: Path = Path.cwd()

# Files to sync
FILES_TO_SYNC: dict[Path, Path] = {
    # ~/
    HOME / ".zshrc": REPO / "root",
    # .config/
    CONFIG / "bspwm" / "bspwmrc": REPO / "config" / "bspwm",
    CONFIG / "sxhkd" / "sxhkdrc": REPO / "config" / "sxhkd",
    CONFIG / "dunst" / "dunstrc": REPO / "config" / "dunst",
    CONFIG / "rofi": REPO / "config" / "rofi",
}


def main() -> int:
    # Delete for redudancy crap
    for folder in ["config", "root"]:
        shutil.rmtree(REPO / folder, ignore_errors=True)

    for source, destination in FILES_TO_SYNC.items():
        # File
        if not source.is_dir():
            destination.mkdir(exist_ok=True, parents=True)
            shutil.copy(source, destination / source.name)

        # Whole folder
        if source.is_dir():
            # destination.mkdir(exist_ok=True, parents=True)
            shutil.copytree(source, destination)

        print(f"Syncing: {source} -> {destination}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
