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

## Aliases

| Alias | Command | Description |
| --- | --- | --- |
| `a` | `add` | Stage a file |
| `aa` | `add -A` | Stage all changes |
| `aap` | `add -A -p` | Stage all changes, interactively hunk by hunk |
| `ab` | `rev-list --left-right --count origin/main...` | Count commits your branch is ahead/behind `origin/main` |
| `amend` | `commit --amend --no-edit` | Amend last commit, keep its message |
| `amend-all` | stage everything, then amend | Stage everything and amend last commit |
| `amend-all-push` | stage, amend, force-push | Stage, amend, and force-push (with lease) |
| `ap` | `add -p` | Stage interactively, hunk by hunk |
| `back` | `checkout -` | Switch to previous branch |
| `c` | `commit` | Commit |
| `candidate` | `checkout candidate` | Switch to the `candidate` branch |
| `cb` | `checkout -b` | Create and switch to a new branch |
| `cc` | `commit -C <commit>` | Reuse another commit's message |
| `chore` | empty commit + push | Create an empty `chore:` commit and push |
| `cm` | `commit -m` | Commit with a message |
| `cma` | stage everything, commit | Stage everything and commit with a message |
| `ch` | `checkout` | Checkout |
| `cp` | `cherry-pick` | Cherry-pick a commit |
| `del` | `branch -D` | Force-delete a local branch |
| `del-r` | `push origin --delete` | Delete a remote branch |
| `ec` | `config --global -e` | Edit the global gitconfig |
| `f` | `fetch` | Fetch |
| `ffmerge` | `merge --ff-only` | Merge only if it can fast-forward |
| `fixup` | `commit --fixup` | Create a `fixup!` commit for autosquash rebase |
| `kill` | delete local + remote branch | Delete a branch locally and on origin |
| `kill-tag` | delete local + remote tag | Delete a tag locally and on origin |
| `lb` | `branch -a` | List all branches (local + remote) |
| `lg` | `log --graph --decorate --oneline` | Compact graph log |
| `lol` | `log --oneline` | One-line log |
| `lol-nt` | `log --format='%C(auto) %h %s'` | One-line log, untruncated |
| `lt` | `tag -l` | List tags |
| `main` | `checkout main` | Switch to `main` |
| `mb` | `merge-base HEAD origin/main` | Common ancestor with `origin/main` |
| `mt` | `mergetool` | Launch mergetool |
| `nb` | `checkout origin/main -b` | Branch off the latest `origin/main` |
| `new` | `log origin/main.. --oneline` | Commits on this branch not yet on `origin/main` |
| `new-f` | `log origin/main..` | Same as `new`, full log format |
| `nukefile` | `filter-branch` on a file | Purge a file from all of history (rewrites every commit/tag) |
| `production` | `checkout production` | Switch to the `production` branch |
| `pu` | `push -u` | Push and set upstream |
| `push-all` | stage, commit, push | Stage, commit ("Updated all the things"), and push everything |
| `pushfwl` | `push --force-with-lease` | Force-push, but abort if remote moved |
| `ra` | `rebase --abort` | Abort an in-progress rebase |
| `rc` | `rebase --continue` | Continue an in-progress rebase |
| `reword` | `commit --amend` | Edit last commit's message |
| `ri` | `rebase -i` | Interactive rebase |
| `rimb` | interactive rebase onto merge-base | Interactive rebase onto merge-base with `origin/main` |
| `rmb` | reset to merge-base | Reset to merge-base with `origin/main` |
| `rm-cached-dir` | `rm -r --cached` | Untrack a directory without deleting it |
| `rom` | `rebase origin/main` | Rebase current branch onto `origin/main` |
| `scrub` | `clean -fd` + `reset --hard` | Discard all uncommitted/untracked changes |
| `scrubx` | `clean -fxd` + `reset --hard` | Scrub, including ignored files too |
| `server` | `git daemon ...` | Serve this repo over the network (allows anonymous push!) |
| `st` | `status` | Status |
| `tagage` | `for-each-ref --sort=taggerdate` | List tags sorted by tagger date |
| `wip` | stage everything, commit "wip" | Stage everything and commit as "wip" |
| `wipit` | wip + push | Same as `wip`, plus push |
