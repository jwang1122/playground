# playground
python playground

## Frequently used GIT commands
to clone a repository from GitHub to your laptop
first got to your workspace root folder, then

```
git clone <paste your git URL here>
```

## Install Package online
```
pip install panada
```

## GitHub Issues

1. cannot upload project to git repository, always pops up user.name and email not set
```
git config --list
git config user.name
git config user.email
git config --global user.name "xxx xxxx"
git config --global user.email "xxxx@gmail.com"
git config user.name "xxxx xxxx"
git config user.email "xxxx@gmail.com"
more ~/.gitconfig
```

2. create a virtual environment
```
python3 -m venv env
source env/bin/activate
```