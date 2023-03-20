# Task Manager V2
### Password manager applciation created with python and deployed to docker

## Table of Contents
* [General Info](#general-info)
* [Technology](#technologies)
* [Requirements](#requirements)
* [Installation and Usage](#installation-and-usage)
* [Notes](#notes)

## General Information
This project is a simple password application created using Python and Sqlite and deployed to docker.
The aim of this project is to create a password manager vault system with my knowlegde on crytography to assist in password storage.

## Technologies
Project is created with:
* Python version: 3.10.0
* Crytography version: 39.0.0
* Inputimeout version: 1.0.4
* Prettytable version: 3.6.0
* Pyfiglet version: 0.8.post1
* Termcolor version: 2.2.0
* SQLite version: 2.6.0

## Requirements
Password Manager V2 (psv2) requires the following to run:
* [Python](https://www.python.org/downloads/) 3.10+
* [Docker](https://www.docker.com/products/docker-desktop/)
* [Git CLI](https://git-scm.com/downloads)

## Installation and Usage
You can install PSV2 using Git CLI:
```console
$ gh repo clone Cyrof/password_manager_2.0
```
OR </br>
You can install PSV2 by downloading the zip file [here](https://github.com/Cyrof/password_manager_2.0/archive/refs/tags/v2.0.zip) or the tar file [here](https://github.com/Cyrof/password_manager_2.0/archive/refs/tags/v2.0.tar.gz).

### To create the docker image and container for this projects:
First cd into the program directory
```console
$ cd path/password_manager_2.0
```
After which run the run.py script automatically get docker to create the docker image and container for it.
```console
$ python run.py
```
OR 
```console
### python3 run.py
```

### Once you run the run.py script, to start using the program:
```console
$ docker start -i psv2
```
### What you will expect to see
Once you run start the program, you should see:
```console
Start? [y/n]: 
```
You will have 30 seconds to enter y or n to start or stop the program if not the program would automatically end. </br>
After the program started it would show:
```console

__        __   _                            _        
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 

 ____  ______     ______  
|  _ \/ ___\ \   / /___ \ 
| |_) \___ \\ \ / /  __) |
|  __/ ___) |\ V /  / __/ 
|_|   |____/  \_/  |_____|


To start, you will have to create a master password. Be careful not to lose it as it is unrecoverable.
Create master password for the program: 
```
OR </br>
If you have created the master password already then it would show:
```console
__        __   _                            _        
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/

 ____  ______     ______
|  _ \/ ___\ \   / /___ \
| |_) \___ \\ \ / /  __) |
|  __/ ___) |\ V /  / __/
|_|   |____/  \_/  |_____|


Enter master password:
```
Once you logged in it should show:
```console

        *Enter 'exit' at any point to exit.*

1) Store a password
2) Update a password
3) Retrieve a password
4) Delete a password
5) Generate a password
6) Erase all passwords
7) Delete all data including master password
Enter a choice: 
```

## Notes
Implementation or usage of this program at your own risk as it is not guaranteed to be correct and efficient. </br>
If there are any features that you would like to see be included or bugs, pleace let me know by creating an issue.
