#!/bin/bash

GIT_REPO=https://github.com/cryptinq/architek/tree/dev

## Check if git is installed & get absolute path

git_path=$(command -v git)

if [ -z "$git_path" ]; then
  echo -e "\033[31mError: Git is not installed. Please install it before running this script.\033[0m"
  exit 1
fi

## Check if Python or Python3 is installed and get the absolute path

python_path=$(command -v python)

if [ -z "$python_path" ]; then
  python_path=$(command -v python3)

  if [ -z "$python_path" ]; then
    echo -e "\033[31mError: Python is not installed. Please install it before running this script.\033[0m"
    exit 1
  fi
fi

## Check if the venv module is installed for Python

if ! "$python_path" -c "import venv" &> /dev/null; then
  echo -e "\033[31mError: The 'venv' module is not installed for Python. Please install it before running this script.\033[0m"
  exit 1
fi

## Clone the repo

read -p "Enter the name of the project: " project_name

git clone "${GITHUB_REPO}" "$project_name"

## Setup venv & install requirements

$python_path -m venv venv
source venv/bin/activate

## Check if pip or pip3 is installed within the venv

if command -v pip &> /dev/null; then
  pip_cmd="pip"
elif command -v pip3 &> /dev/null; then
  pip_cmd="pip3"
else
  echo -e "\033[31mError: Neither 'pip' nor 'pip3' is installed within the virtual environment.\033[0m"
  exit 1
fi

$pip_cmd install -r requirements.txt

## Everything seems OK

echo "Architek installed successfully !"
echo ""
echo "Run 'source venv/bin/activate' to activate venv"
echo "Run 'python console help' for more help"
echo ""
echo "Happy python coding !"
echo "$GIT_REPO"

deactivate

