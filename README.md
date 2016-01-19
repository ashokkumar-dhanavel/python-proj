# python-proj
## About the project

It’s nothing more than a simple version of grep command in linux system. The purpose of this project is to make easier for the user to search a word or multpile words from the give path.

## SetUp

Download the project from the github using https or git clone command,

    https://github.com/ashokkumar-dhanavel/python-proj.git

                     or
    git clone git@github.com:ashokkumar-dhanavel/python-proj.git

## Pre-requisites for testing the project


The following python packages are required for testing the project

1) nose

command to install nose package "pip install nose"

## Project Installation

After downloading the project from the github location setup the project using the command,

python setup.py install

## Logfind command usage

usage: logfind.py [-h] p s

Find the String from the log files

positional arguments:
  p           directory path
  s           keyword to find from the log files. Accept multiple words
              example 'Hello world'

optional arguments:
  -h, --help  show this help message and exit
