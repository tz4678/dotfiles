# Dotfiles

Добавляем alias:

```zsh
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'
```

Отключаем вывод untracked files при вызове `dotfiles status`:

```zsh
dotfiles config --local status.showUntrackedFiles no
```

Клонируем репозиторий:

```zsh
git clone --bare git@github.com:tz4678/dotfiles.git $HOME/.dotfiles
```

Развертывание на новой машине:

```zsh
dotfiles checkout
```
