# install dir
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="darkblood"
COMPLETION_WAITING_DOTS="true"
DISABLE_UNTRACKED_FILES_DIRTY="true"

plugins=(git)

# Load ohmyzsh (soyjak)
source $ZSH/oh-my-zsh.sh

# My shit
# Path
path+=/home/junko/.local/bin
path+=/run/media/junko/2nd/Tools/Scripts/
path=('/home/junko/bin' $path)

# Colorscheme
(cat ~/.cache/wal/sequences &)

# Wasmer
export WASMER_DIR="/home/junko/.wasmer"
[ -s "$WASMER_DIR/wasmer.sh" ] && source "$WASMER_DIR/wasmer.sh"

# thing
export FLYCTL_INSTALL="/home/junko/.fly"
export PATH="$FLYCTL_INSTALL/bin:$PATH"

# thing
eval $(thefuck --alias)\

tere() {
    local result=$(command tere "$@")
    [ -n "$result" ] && cd -- "$result"
}

