# AutoGitPython

Small Python Script for automatically create a new GitHub Repo for you Projects to work with

## Requirements

- [Python (3 or higher)](https://www.python.org/downloads/)
- pip (already comes with Python cf. [pip-documentation](https://pip.pypa.io/en/stable/installing/))

## Setup

```bash
git clone "https://github.com/TheGlitchHam/AutoGitPython.git"
cd AutoGitPython
python3 -m venv env (creates virtual environment)
.\env\Scripts\activate (activates it)
pip install -r requirements.txt
```

## Usage

```bash
python AutoGit.py
```

You need to have a valid GitHub Token to access github. You can create an access token on your GitHub-profile settings at

> `settings\developer settings\personal access token`

or see the respective [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token).

Either enter it manually, or put it into a file called `token` (without file ending) into the same directory as the Python Script
