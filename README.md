# Dotfiles

Add alias:

```zsh
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'
```

Disable git status **untracked files**:

```zsh
dotfiles config --local status.showUntrackedFiles no
```

Deployment:

```zsh
git clone --bare git@github.com:tz4678/dotfiles.git $HOME/.dotfiles
dotfiles checkout
```

## Gallery

![image](https://user-images.githubusercontent.com/12753171/110113674-7c747100-7dc4-11eb-94f0-503d7d262dc3.png)
![image](https://user-images.githubusercontent.com/12753171/110150539-6ed4e080-7df0-11eb-8812-2c0001e5d74c.png)
