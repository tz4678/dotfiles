# Dotfiles

## Установка

Добавляем alias:

```zsh
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'
```

Отключаем вывод **untracked files** при вызове `dotfiles status`:

```zsh
dotfiles config --local status.showUntrackedFiles no
```

Развертывание на другой машине:

```zsh
git clone --bare git@github.com:tz4678/dotfiles.git $HOME/.dotfiles
dotfiles checkout
```

## Docker-Compose

```zsh
$ systemctl --user enable --now docker-compose@myservice
```

## Галерея

### Gnome Terminal

![image](https://user-images.githubusercontent.com/12753171/108596051-98731e00-7393-11eb-94bd-71d655c88149.png)

### Vim

![image](https://user-images.githubusercontent.com/12753171/108596258-e2103880-7394-11eb-9249-bb4a5be9e007.png)

### Pet

Менеджер сниппетов для терминала. Вызывается по `^S`.

![image](https://user-images.githubusercontent.com/12753171/108596508-9199da80-7396-11eb-97ca-ddbdf46b7904.png)

![image](https://user-images.githubusercontent.com/12753171/108596568-ea697300-7396-11eb-9790-550f4818f834.png)

### [PGAdmin](http://localhost:5050)

![image](https://user-images.githubusercontent.com/12753171/108596104-ea1ba880-7393-11eb-83bb-15a5dfdaf343.png)

### [Локальная Wiki](http://localhost:3000)

![image](https://user-images.githubusercontent.com/12753171/108596014-3f0aef00-7393-11eb-8108-e7937af55aee.png)
