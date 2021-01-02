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

### manage.py

##### Run code

```bash
python3 manage.py [add/update/remove/list] [--optional argument]
```

##### Help
```console
python3 manage.py --help
```

```console
(mgenv) python3 manage.py --help
usage: manage.py [-h] [--name NAME] [--deadline DEADLINE] [--description DESCRIPTION] [--all] [--today] a [hash]

positional arguments:
  operation                     options to operate tasks
  hash

optional arguments:
  -h, --help            show this help message and exit
  --name NAME           Name of task
  --deadline DEADLINE   Time of the task's deadline (format YYYY-MM-DD)
  --description DESCRIPTION
                        Desription of the task
  --all                 list all remaining tasks
  --today               list all tasks with today deadline

Examples:
python3 manage.py add --name "Cleaning" --deadline 2020-06-13 --description "Clean the bathroom"
python3 manage.py update --deadline "2020-07-20" dce894a5e3fda958da80bc8098c3cfea
python3 manage.py remove dce894a5e3fda958da80bc8098c3cfea
python3 manage.py list --all
```

## Chapter2

##### Run code to see answer

```console
python3 chapter2.py
```