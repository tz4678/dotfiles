# Dotfiles

Add alias:

```zsh
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'
```

Disable **untracked files**:

```zsh
dotfiles config --local status.showUntrackedFiles no
```

Deployment:

```zsh
git clone --bare git@github.com:tz4678/dotfiles.git $HOME/.dotfiles
dotfiles checkout
```
