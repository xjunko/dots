#!/bin/bash
# Linux script for me by me, dont bother using it.

export PATH="$PATH:/home/junko/.local/bin/"

#python -m pywal -i ~/Pictures/Pape/ &> ~/Pictures/Pape/output.txt &&
#oomox-cli /home/junko/.cache/wal/colors-oomox && oomox-archdroid-icons-cli  /home/junko/.cache/wal/colors-oomox &&
#notify-send Wallpaper "GTK and Icons changed"

/bin/bash /home/junko/.config/polybar/launch.sh --cuts &&
/bin/bash ~/.config/polybar/cuts/scripts/pywal.sh /home/junko/Pictures/Pape/ &> ~/Pictures/Pape/output.txt &&
/bin/bash ~/.config/polybar/launch.sh --cuts &&

notify-send Wallpaper "Colorschemes changed"
