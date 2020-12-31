import argparse
import textwrap
import datetime as dt

def valid_date(s):
    try:
        return dt.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = f"Not a valid date: '{s}'"
        raise argparse.ArgumentTypeError(msg)

parser = argparse.ArgumentParser(prog='manage.py', formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent('''\
        Examples:
        python3 manage.py add --name "Cleaning" --deadline 2020-06-13 --description "Clean the bathroom"
        python3 manage.py update --deadline "2020-07-20" dce894a5e3fda958da80bc8098c3cfea
        python3 manage.py remove dce894a5e3fda958da80bc8098c3cfea
        python3 manage.py list --all
         '''),
        usage = "python3 manage.py operation [-h] [--name NAME] [--deadline DEADLINE] [--description DESCRIPTION] [--all] [--today] [hash]"
         )

parser.add_argument("operation", type=str, help="options to operate tasks list")
parser.add_argument("--name", type=str, required=False , help="Name of task", dest='name')
parser.add_argument('--deadline', type=valid_date, required=False , help="Time of the task's deadline (format YYYY-MM-DD)")
parser.add_argument('--description', required=False, help="Desription of the task")
parser.add_argument('--all', required=False, action='store_true', help= 'list all remaining tasks')
parser.add_argument('--today', required=False, action='store_true', help = 'list all tasks with today deadline')
parser.add_argument('hash', nargs='?', type=str, default = '3.14', help = 'hashcode of task')

options = vars(parser.parse_intermixed_args())