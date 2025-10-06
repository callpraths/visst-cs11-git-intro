# Crawl

Just learn these two commands to be able to "save changes"

## Initialize

```sh
git init <dirname>
```

## Save

```sh
git commit -a
```

## What is unsaved again?

```sh
git diff
```

# First run setup

```sh
git config --global user.name "Your Name"
git config --global user.email "Your email"
git config --global core.editor vim  # Or whatever you want. `nano` if you really want to.
```

# Walk

The real power comes when you're unable to peek at history and undo changes:

## Undo

```sh
git checkout -f     # If throwing away uncommited work
git revert HEAD     # If already commited.
```

## What have I done so far?

```sh
git log             # All of the history
git show <commit>   # Details of a commit
```
