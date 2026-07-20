# git-config

My global git configuration.

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/96daysleft/git-config/main/install.sh | bash
```

This merges the settings into `~/.gitconfig` without overwriting it: any key you already have set locally is left alone, and anything missing is added.

Then edit `~/.gitconfig` and fill in your name and email:

```sh
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
