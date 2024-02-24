#!/bin/bash

GIT_REPO="https://github.com/cryptinq/architek.git"

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

echo "git clone --branch dev \"${GIT_REPO}\" \"$project_name\""

git clone --branch dev "${GIT_REPO}" "$project_name"

cd $project_name

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

echo ""
echo " --- Architek installed successfully !"
echo ""
echo " - Next Steps :"
echo ""
echo "   Run 'source venv/bin/activate' to activate virtual environment"
echo "   Edit the configuration file on the config/ folder"
echo "   Define your schemas in database/schema/ folder"
echo "   Run 'python console database:create' to create database"
echo "   Run 'python console entity:generate' to generate corresponding entities"
echo ""
echo "   Run 'python console help' for more help"
echo ""
echo " -> Happy coding with the architek framework ! <-"

deactivate

