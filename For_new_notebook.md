[Install Visual Studia for windows](https://visualstudio.microsoft.com/ru/)

Angular

export NVM_DIR="$HOME/.nvm" && (
 git clone https://github.com/nvm-sh/nvm.git "$NVM_DIR"
 cd "$NVM_DIR"
 git checkout `git describe --abbrev=0 --tags --match "v[0-9]*" $(git rev-list --tags --max-count=1)`
) && \. "$NVM_DIR/nvm.sh"

# Install actual node version:
nvm i 12

JAVA

