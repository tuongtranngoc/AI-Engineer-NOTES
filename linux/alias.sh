# On macOS
brew install rsync
nano ~/.zshrc
alias copy="rsync -a -v -z --progress --partial"
source ~/.zshrc
