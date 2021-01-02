# Skychallange

My solution of Skychallange tasks.

## Installation

Be sure you have python 3.8 installed. 

In terminal:
```console
skyenv\Scripts\activate
```

This runs the python environment with the necessary requirements to run the application
Be sure you are using the python environment ```skyenv```.

Upgrade pip and modules
```console
pip install --upgrade pip
pip install -r requirements.txt
```

# Running the tasks

All of scripts are located in folders of the following names.

## Chapter1

Folder structure

```
│   manage.py
│
└───package
    │   args.py
    │   data.py
    │   __init__.py
```

file ``` manage.py ``` is the main file which starts the whole program

##### Run app

Make sure you are in ```Chapter1``` folder

```bash
python3 manage.py [add/update/remove/list] [--optional argument]
```
##### Examples of usage

##### Add task

Adding the task you can specify its name ``` --name ```, deadline day ``` --deadline ``` and add short description of the task ``` --description ```

```bash
python3 manage.py add --name "Cleaning" --deadline "2021-01-15" --description "Clean the bathroom"
```

##### Update task

You can update your task by

```bash
python3 manage.py update --deadline "2021-01-16" dce894a5e3fda958da80bc8098c3cfea
```

##### Remove task

Remove the task by specifying its hash code

```bash
python3 manage.py remove dce894a5e3fda958da80bc8098c3cfea
```

##### List tasks

You can list all tasks by:

```bash
python3 manage.py list --all
```

or tasks with today's deadline

```bash
python3 manage.py list --today
```

##### Help

Type this to get more help with running the application

```console
python3 manage.py --help
```

## Chapter2

##### Run code to see answer

```console
python3 chapter2.py
```
